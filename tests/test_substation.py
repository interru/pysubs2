"""
pysubs2.formats.substation tests

"""

from __future__ import unicode_literals
from pysubs2 import SSAFile, SSAEvent, SSAStyle, make_time

SIMPLE_ASS_REF = """
[Script Info]
; Script generated by pysubs2
; https://pypi.python.org/pypi/pysubs2
WrapStyle: 0
ScaledBorderAndShadow: yes
Collisions: Normal
My Custom Info: Some: Test, String.
ScriptInfo: v4.00+

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Arial,20.0,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,0,0,0,0,100.0,100.0,0.0,0.0,1,2.0,2.0,2,10,10,10,1
Style: left,Arial,20.0,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100.0,100.0,0.0,0.0,1,2.0,2.0,7,10,10,10,1
Style: topleft,Arial,20.0,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,0,0,0,0,100.0,100.0,0.0,0.0,1,2.0,2.0,4,10,10,10,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.00,0:01:00.00,Default,,0,0,0,,An, example, subtitle.
Comment: 0,0:00:00.00,0:01:00.00,Default,,0,0,0,,You can't see this one.
Dialogue: 0,0:01:00.00,0:02:00.00,Default,,0,0,0,,Subtitle number\\Ntwo.
"""

SIMPLE_SSA_REF = """\
[Script Info]
; Script generated by pysubs2
; https://pypi.python.org/pypi/pysubs2
WrapStyle: 0
ScaledBorderAndShadow: yes
Collisions: Normal
My Custom Info: Some: Test, String.
ScriptInfo: v4.00

[V4 Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, TertiaryColour, BackColour, Bold, Italic, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, AlphaLevel, Encoding
Style: Default,Arial,20.0,16777215,255,0,0,0,0,1,2.0,2.0,2,10,10,10,0,1
Style: left,Arial,20.0,16777215,255,0,0,-1,0,1,2.0,2.0,5,10,10,10,0,1
Style: topleft,Arial,20.0,16777215,255,0,0,0,0,1,2.0,2.0,9,10,10,10,0,1

[Events]
Format: Marked, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: Marked=0,0:00:00.00,0:01:00.00,Default,,0,0,0,,An, example, subtitle.
Comment: Marked=0,0:00:00.00,0:01:00.00,Default,,0,0,0,,You can't see this one.
Dialogue: Marked=0,0:01:00.00,0:02:00.00,Default,,0,0,0,,Subtitle number\\Ntwo.
"""

def build_ref():
    subs = SSAFile()
    subs.info["My Custom Info"] = "Some: Test, String."
    subs.styles["left"] = SSAStyle(alignment=7, bold=True)
    subs.styles["topleft"] = SSAStyle(alignment=4)
    subs.append(SSAEvent(start=0, end=make_time(m=1), text="An, example, subtitle."))
    subs.append(SSAEvent(start=0, end=make_time(m=1), type="Comment", text="You can't see this one."))
    subs.append(SSAEvent(start=make_time(m=1), end=make_time(m=2), text="Subtitle number\\Ntwo."))
    return subs

def test_simple_write():
    subs = build_ref()
    assert subs.to_string("ass").strip() == SIMPLE_ASS_REF.strip()
    assert subs.to_string("ssa").strip() == SIMPLE_SSA_REF.strip()

def test_simple_read():
    ref = build_ref()
    subs1 = SSAFile.from_string(SIMPLE_ASS_REF)
    subs2 = SSAFile.from_string(SIMPLE_SSA_REF)

    assert ref.equals(subs1)
    assert ref.equals(subs2)
