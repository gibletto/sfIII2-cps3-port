#!/usr/bin/env python3
"""Copies the game's data files so they are laid out in memory as on the arcade board.

    python port/tools/host_data.py [--big-endian] <out dir> <data .c files...>

The game finds some data by position (a script's header is the array just before it, sound sequences are
offsets into the arrays that follow). GCC pads larger arrays, so each array definition gets an explicit
alignment equal to its element's. The build compiles the copies; games/sf2i is left as it is.
"""
import pathlib, re, sys

# u16 and u32 tables the game reads a byte at a time: byte-swapped on little-endian hosts so the bytes come out
# in the board's order. sc_chr_data's readers run on into the tables after it (data/chr_data_b.c).
BYTE_IMAGES = {"sys_font_cg": 2, "sc_chr_data": 2, "default_face_wide_chr": 2, "gill_face_wide_chr": 2,
               "config_jp_chr_f400": 4}
LITTLE_ENDIAN = True    # --big-endian for big-endian targets, which take the tables as they are
NUMBER = re.compile(r"\b(0[xX][0-9A-Fa-f]+|\d+)\b")


def swap16(m):
    v = int(m.group(1), 0) & 0xFFFF
    return "0x%04X" % (((v & 0xFF) << 8) | (v >> 8))


def swap32(m):
    v = int(m.group(1), 0) & 0xFFFFFFFF
    return "0x%08X" % int.from_bytes(v.to_bytes(4, "big"), "little")


DEF = re.compile(r"^(?P<decl>(?:static\s+)?const\s+[^=;(]*?\b(?P<name>[A-Za-z_]\w*)\s*(?:\[[^\]]*\])+)\s*=")


def transform(text, src):
    out = [f'#line 1 "{src.as_posix()}"']
    image = None
    for line in text.splitlines():
        m = DEF.match(line)
        if m and not line.startswith("static"):
            decl, name = m.group("decl"), m.group("name")
            rest = line[m.end("decl"):]
            line = f"extern {decl}; {decl} __attribute__((aligned(__alignof__({name}[0]))))" + rest
            if name in BYTE_IMAGES:
                image = name
        elif image:
            if line.startswith("};"):
                image = None
            elif LITTLE_ENDIAN:
                code, sep, comment = line.partition("/*")
                line = NUMBER.sub(swap16 if BYTE_IMAGES[image] == 2 else swap32, code) + sep + comment
        out.append(line)
    return "\n".join(out) + "\n"


def main():
    global LITTLE_ENDIAN
    args = sys.argv[1:]
    if args and args[0] == "--big-endian":
        LITTLE_ENDIAN = False
        args = args[1:]
    outdir = pathlib.Path(args[0])
    outdir.mkdir(parents=True, exist_ok=True)
    for name in args[1:]:
        src = pathlib.Path(name).resolve()
        text = transform(src.read_text(encoding="utf-8", errors="surrogateescape"), src)
        dst = outdir / src.name
        if not dst.exists() or dst.read_text(encoding="utf-8", errors="surrogateescape") != text:
            dst.write_text(text, encoding="utf-8", errors="surrogateescape", newline="\n")


if __name__ == "__main__":
    main()
