from ...utils import ep_assert

# fmt: off
"""
TranWire.grp
"""
TranWire32 = (0x00070040, 0x03562014, 0x01030000, 0x05C51E17, 0x05000000, 0x07B63520, 0x02020000, 0x0C213C1E, 0x05010000, 0x1185091D, 0x00010000, 0x1291403F, 0x05010000, 0x1B28091D, 0x01030000, 0x1C2A201C, 0x05010000, 0x1EF7091D, 0x05010000, 0x1EF7091D, 0x00040000, 0x1FFE2018, 0x05010000, 0x1EF7091D, 0x05010000, 0x1EF7091D, 0x02010000, 0x22B91C1A, 0x05010000, 0x256F091D, 0x02060000, 0x267B1E12, 0x00030000, 0x28532017, 0x02020000, 0x2A603C1E, 0x05010000, 0x2FC4091D, 0x05000000, 0x07B63520, 0x00070000, 0x30D22014, 0x02020000, 0x2A603C1E, 0x05010000, 0x2FC4091D, 0x00010000, 0x3341403F, 0x05010000, 0x1B28091D, 0x05010000, 0x1B28091D, 0x05010000, 0x1B28091D, 0x05010000, 0x1B28091D, 0x05010000, 0x1B28091D, 0x05010000, 0x1B28091D, 0x00000000, 0x3BD6403C, 0x05010000, 0x4561091D, 0x00040000, 0x1FFE2018, 0x00070000, 0x30D22014, 0x01060000, 0x46672017, 0x05050000, 0x49271615, 0x05010000, 0x4A59091D, 0x00060000, 0x4B5A1F17, 0x06000000, 0x4D1C351F, 0x06000000, 0x50A13440, 0x01030000, 0x55B91E1B, 0x02000000, 0x57A71E20, 0x05010000, 0x5A23091D, 0x05010000, 0x5A23091D, 0x05010000, 0x5A23091D, 0x05010000, 0x5A23091D, 0x06010000, 0x5B2D321F, 0x05010000, 0x5DAE091D, 0x06000000, 0x50A13440, 0x0B070000, 0x5EB22732, 0x00010000, 0x62C0201C, 0x01020000, 0x65421F1B, 0x06010000, 0x5B2D321F, 0x06000000, 0x4D1C351F, 0x00060000, 0x4B5A1F17, 0x05010000, 0x1EF7091D, 0x05010000, 0x1EF7091D, 0x05010000, 0x1EF7091D, 0x03000000, 0x675A3B40, 0x05010000, 0x1EF7091D, 0x05010000, 0x1EF7091D, 0x00000000, 0x6F32401F, 0x01000000, 0x74B93D3C, 0x00030000, 0x7C39403C, 0x00010000, 0x8524201F, 0x00010000, 0x882A401F, 0x01070000, 0x8EB73E31, 0x00000000, 0x96684020, 0x03010000, 0x9CD53D3C, 0x05010000, 0x5A23091D, 0x05010000, 0x5A23091D, 0x05010000, 0x5A23091D, 0x05010000, 0x5A23091D, 0x05010000, 0x5A23091D, 0x00000000, 0x6F32401F, 0x00000000, 0x6F32401F, 0x03010000, 0x9CD53D3C, 0x00010000, 0xA5F2401F, 0x01070000, 0x8EB73E31, 0x00000000, 0x96684020, 0x00000000, 0xAC7D2020, 0x06030000, 0xAFB3383A, 0x05010000, 0xB6CE091D, 0x06030000, 0xAFB3383A, 0x05010000, 0xB7D8091D, 0x05010000, 0xB7D8091D, 0x05010000, 0xB7D8091D, 0x05010000, 0xB7D8091D, 0x01030000, 0x05C51E17, 0x03000000, 0xB8D91B20, 0x04000000, 0xBB75181F, 0x06000000, 0xBCEB3440, 0x06000000, 0xBCEB3440, 0x00010000, 0xC2981F1B, 0x05010000, 0xB7D8091D, 0x05000000, 0xC47D1520, 0x05010000, 0xC6311A19, 0x05010000, 0xB7D8091D, 0x05010000, 0xB7D8091D, 0x01030000, 0x05C51E17, 0x01030000, 0x05C51E17, 0x06000000, 0xBCEB3440, 0x05010000, 0x1EF7091D, 0x06000000, 0xBCEB3440, 0x01030000, 0x05C51E17, 0x05010000, 0xB7D8091D, 0x00400000, 0x00510047)
TranWire64 = (0x00070040, 0x04FE2014, 0x01030000, 0x076D1E17, 0x05000000, 0x095E3520, 0x02020000, 0x0DC93C1E, 0x05010000, 0x132D091D, 0x00010000, 0x1439403F, 0x05010000, 0x1CD0091D, 0x01030000, 0x1DD2201C, 0x05010000, 0x209F091D, 0x05010000, 0x209F091D, 0x00040000, 0x21A62018, 0x05010000, 0x209F091D, 0x05010000, 0x209F091D, 0x02010000, 0x24611C1A, 0x05010000, 0x2717091D, 0x02060000, 0x28231E12, 0x00030000, 0x29FB2017, 0x02020000, 0x2C083C1E, 0x05010000, 0x316C091D, 0x05000000, 0x095E3520, 0x00070000, 0x327A2014, 0x02020000, 0x2C083C1E, 0x05010000, 0x316C091D, 0x00010000, 0x34E9403F, 0x05010000, 0x1CD0091D, 0x05010000, 0x1CD0091D, 0x05010000, 0x1CD0091D, 0x05010000, 0x1CD0091D, 0x05010000, 0x1CD0091D, 0x05010000, 0x1CD0091D, 0x00000000, 0x3D7E403C, 0x05010000, 0x4709091D, 0x00040000, 0x21A62018, 0x00070000, 0x327A2014, 0x01060000, 0x480F2017, 0x05050000, 0x4ACF1615, 0x05010000, 0x4C01091D, 0x00060000, 0x4D021F17, 0x06000000, 0x4EC4351F, 0x06000000, 0x52493440, 0x01030000, 0x57611E1B, 0x02000000, 0x594F1E20, 0x05010000, 0x5BCB091D, 0x05010000, 0x5BCB091D, 0x05010000, 0x5BCB091D, 0x05010000, 0x5BCB091D, 0x06010000, 0x5CD5321F, 0x05010000, 0x5F56091D, 0x06000000, 0x52493440, 0x0B070000, 0x605A2732, 0x00010000, 0x6468201C, 0x01020000, 0x66EA1F1B, 0x06010000, 0x5CD5321F, 0x06000000, 0x4EC4351F, 0x00060000, 0x4D021F17, 0x05010000, 0x209F091D, 0x05010000, 0x209F091D, 0x05010000, 0x209F091D, 0x03000000, 0x69023B40, 0x05010000, 0x209F091D, 0x05010000, 0x209F091D, 0x00000000, 0x70DA401F, 0x01000000, 0x76613D3C, 0x00030000, 0x7DE1403C, 0x00010000, 0x86CC201F, 0x00010000, 0x89D2401F, 0x01070000, 0x905F3E31, 0x00000000, 0x98104020, 0x03010000, 0x9E7D3D3C, 0x05010000, 0x5BCB091D, 0x05010000, 0x5BCB091D, 0x05010000, 0x5BCB091D, 0x05010000, 0x5BCB091D, 0x05010000, 0x5BCB091D, 0x00000000, 0x70DA401F, 0x00000000, 0x70DA401F, 0x03010000, 0x9E7D3D3C, 0x00010000, 0xA79A401F, 0x01070000, 0x905F3E31, 0x00000000, 0x98104020, 0x00000000, 0xAE252020, 0x06030000, 0xB15B383A, 0x05010000, 0xB876091D, 0x06030000, 0xB15B383A, 0x05010000, 0xB980091D, 0x05010000, 0xB980091D, 0x05010000, 0xB980091D, 0x05010000, 0xB980091D, 0x01030000, 0x076D1E17, 0x03000000, 0xBA811B20, 0x04000000, 0xBD1D181F, 0x06000000, 0xBE933440, 0x06000000, 0xBE933440, 0x00010000, 0xC4401F1B, 0x05010000, 0xB980091D, 0x05000000, 0xC6251520, 0x05010000, 0xC7D91A19, 0x05010000, 0xB980091D, 0x05010000, 0xB980091D, 0x01030000, 0x076D1E17, 0x01030000, 0x076D1E17, 0x06000000, 0xBE933440, 0x05010000, 0x209F091D, 0x06000000, 0xBE933440, 0x01030000, 0x076D1E17, 0x05010000, 0xB980091D, 0x00400000, 0x00510047)
ep_assert(len(TranWire32) == len(TranWire64) == (106 + 1) * 2)

"""
GrpWire.grp
"""
GrpWire32 = (0x00070020, 0x041E2014, 0x01030000, 0x068D1E17, 0x03000000, 0x087E1C20, 0x00030000, 0x0AD5201C, 0x05010000, 0x0DA2091D, 0x00010000, 0x0EA6201F, 0x05010000, 0x1176091D, 0x00030000, 0x127D201C, 0x04000000, 0x154A1920, 0x00000000, 0x17E61F1F, 0x00040000, 0x1AF22018, 0x00000000, 0x1DA91F20, 0x01000000, 0x20E81E20, 0x00020000, 0x2432201C, 0x05010000, 0x2774091D, 0x02060000, 0x287B1E12, 0x00030000, 0x2A532017, 0x00030000, 0x0AD5201C, 0x05010000, 0x2C60091D, 0x03000000, 0x087E1C20, 0x00070000, 0x2D672014, 0x04000000, 0x2FD81920, 0x00000000, 0x17E61F1F, 0x00010000, 0x0EA6201F, 0x05010000, 0x3276091D, 0x00010000, 0x337D1F1D, 0x05010000, 0x2C60091D, 0x05010000, 0x2C60091D, 0x01000000, 0x20E81E20, 0x01000000, 0x20E81E20, 0x00010000, 0x337D1F1D, 0x05010000, 0x366A091D, 0x00040000, 0x37742018, 0x00070000, 0x3A2F2014, 0x00060000, 0x3C9E2017, 0x00020000, 0x3F5C201D, 0x02000000, 0x414C1C20, 0x00040000, 0x43B72018, 0x00030000, 0x45A1201C, 0x03000000, 0x47BD1B20, 0x01030000, 0x49E11E1B, 0x01000000, 0x4BCF1E20, 0x00030000, 0x4E4B201C, 0x02000000, 0x51421C20, 0x02000000, 0x534B1C20, 0x00000000, 0x55542020, 0x01000000, 0x57ED1F20, 0x02010000, 0x59B31C1E, 0x03000000, 0x47BD1B20, 0x00000000, 0x55542020, 0x00010000, 0x5B93201C, 0x01020000, 0x5E151F1B, 0x01000000, 0x57ED1F20, 0x00030000, 0x45A1201C, 0x00040000, 0x602D2018, 0x02000000, 0x62171C20, 0x02000000, 0x534B1C20, 0x00030000, 0x4E4B201C, 0x02000000, 0x641F1D20, 0x02000000, 0x66DE1C20, 0x02010000, 0x69571B1D, 0x00000000, 0x6B9E201E, 0x01000000, 0x6E541E1E, 0x01020000, 0x70C51F1E, 0x00010000, 0x7396201F, 0x00010000, 0x769C201F, 0x01040000, 0x79F11F18, 0x00000000, 0x7C862020, 0x00000000, 0x7FDC2020, 0x04000000, 0x832E1B20, 0x00000000, 0x85D81F20, 0x00000000, 0x8895201F, 0x00000000, 0x8B7D2020, 0x04000000, 0x8EB61920, 0x00000000, 0x6B9E201E, 0x00000000, 0x6B9E201E, 0x00000000, 0x7FDC2020, 0x00010000, 0x769C201F, 0x01040000, 0x79F11F18, 0x00000000, 0x7C862020, 0x00000000, 0x90C21F20, 0x02000000, 0x93811D1F, 0x00000000, 0x8B7D2020, 0x02000000, 0x93811D1F, 0x01010000, 0x961D1D1C, 0x05010000, 0x987D091D, 0x00000000, 0x8895201F, 0x05010000, 0x366A091D, 0x00000000, 0x85D81F20, 0x03000000, 0x99841B20, 0x04000000, 0x9C20181F, 0x03000000, 0x9D961A20, 0x03000000, 0x9D961A20, 0x00010000, 0x9F7D1F1B, 0x00000000, 0xA1621F20, 0x05000000, 0xA30C1520, 0x05010000, 0xA4C01A19, 0x08020000, 0xA6920E1A, 0x00000000, 0x6B9E201E, 0x01030000, 0x068D1E17, 0x01030000, 0x068D1E17, 0x03000000, 0x9D961A20, 0x01000000, 0x20E81E20, 0x03000000, 0x9D961A20, 0x01030000, 0x068D1E17, 0x05010000, 0xA7A9091D, 0x02000000, 0xA8B31D20, 0x05010000, 0xABAF091D, 0x05010000, 0xABAF091D, 0x05010000, 0xABAF091D, 0x05010000, 0xABAF091D, 0x01000000, 0xACB61F20, 0x05010000, 0xAFF7091D, 0x01000000, 0xB0FD1F20, 0x00000000, 0xB4602020, 0x05010000, 0xB7A5091D, 0x05000000, 0xB8AB1820, 0x05010000, 0xBB3A091D, 0x05010000, 0xBB3A091D, 0x05010000, 0xBB3A091D, 0x05010000, 0xBB3A091D, 0x05010000, 0xBB3A091D, 0x05000000, 0xBC431720, 0x05010000, 0x366A091D, 0x05010000, 0x366A091D, 0x05010000, 0x366A091D, 0x05010000, 0x366A091D, 0x05010000, 0x366A091D, 0x05010000, 0x366A091D, 0x05010000, 0x366A091D, 0x05010000, 0x366A091D, 0x00400000, 0x00510047)
GrpWire64 = (0x00070020, 0x062A2014, 0x01030000, 0x08991E17, 0x03000000, 0x0A8A1C20, 0x00030000, 0x0CE1201C, 0x05010000, 0x0FAE091D, 0x00010000, 0x10B2201F, 0x05010000, 0x1382091D, 0x00030000, 0x1489201C, 0x04000000, 0x17561920, 0x00000000, 0x19F21F1F, 0x00040000, 0x1CFE2018, 0x00000000, 0x1FB51F20, 0x01000000, 0x22F41E20, 0x00020000, 0x263E201C, 0x05010000, 0x2980091D, 0x02060000, 0x2A871E12, 0x00030000, 0x2C5F2017, 0x00030000, 0x0CE1201C, 0x05010000, 0x2E6C091D, 0x03000000, 0x0A8A1C20, 0x00070000, 0x2F732014, 0x04000000, 0x31E41920, 0x00000000, 0x19F21F1F, 0x00010000, 0x10B2201F, 0x05010000, 0x3482091D, 0x00010000, 0x35891F1D, 0x05010000, 0x2E6C091D, 0x05010000, 0x2E6C091D, 0x01000000, 0x22F41E20, 0x01000000, 0x22F41E20, 0x00010000, 0x35891F1D, 0x05010000, 0x3876091D, 0x00040000, 0x39802018, 0x00070000, 0x3C3B2014, 0x00060000, 0x3EAA2017, 0x00020000, 0x4168201D, 0x02000000, 0x43581C20, 0x00040000, 0x45C32018, 0x00030000, 0x47AD201C, 0x03000000, 0x49C91B20, 0x01030000, 0x4BED1E1B, 0x01000000, 0x4DDB1E20, 0x00030000, 0x5057201C, 0x02000000, 0x534E1C20, 0x02000000, 0x55571C20, 0x00000000, 0x57602020, 0x01000000, 0x59F91F20, 0x02010000, 0x5BBF1C1E, 0x03000000, 0x49C91B20, 0x00000000, 0x57602020, 0x00010000, 0x5D9F201C, 0x01020000, 0x60211F1B, 0x01000000, 0x59F91F20, 0x00030000, 0x47AD201C, 0x00040000, 0x62392018, 0x02000000, 0x64231C20, 0x02000000, 0x55571C20, 0x00030000, 0x5057201C, 0x02000000, 0x662B1D20, 0x02000000, 0x68EA1C20, 0x02010000, 0x6B631B1D, 0x00000000, 0x6DAA201E, 0x01000000, 0x70601E1E, 0x01020000, 0x72D11F1E, 0x00010000, 0x75A2201F, 0x00010000, 0x78A8201F, 0x01040000, 0x7BFD1F18, 0x00000000, 0x7E922020, 0x00000000, 0x81E82020, 0x04000000, 0x853A1B20, 0x00000000, 0x87E41F20, 0x00000000, 0x8AA1201F, 0x00000000, 0x8D892020, 0x04000000, 0x90C21920, 0x00000000, 0x6DAA201E, 0x00000000, 0x6DAA201E, 0x00000000, 0x81E82020, 0x00010000, 0x78A8201F, 0x01040000, 0x7BFD1F18, 0x00000000, 0x7E922020, 0x00000000, 0x92CE1F20, 0x02000000, 0x958D1D1F, 0x00000000, 0x8D892020, 0x02000000, 0x958D1D1F, 0x01010000, 0x98291D1C, 0x05010000, 0x9A89091D, 0x00000000, 0x8AA1201F, 0x05010000, 0x3876091D, 0x00000000, 0x87E41F20, 0x03000000, 0x9B901B20, 0x04000000, 0x9E2C181F, 0x03000000, 0x9FA21A20, 0x03000000, 0x9FA21A20, 0x00010000, 0xA1891F1B, 0x00000000, 0xA36E1F20, 0x05000000, 0xA5181520, 0x05010000, 0xA6CC1A19, 0x08020000, 0xA89E0E1A, 0x00000000, 0x6DAA201E, 0x01030000, 0x08991E17, 0x01030000, 0x08991E17, 0x03000000, 0x9FA21A20, 0x01000000, 0x22F41E20, 0x03000000, 0x9FA21A20, 0x01030000, 0x08991E17, 0x05010000, 0xA9B5091D, 0x02000000, 0xAABF1D20, 0x05010000, 0xADBB091D, 0x05010000, 0xADBB091D, 0x05010000, 0xADBB091D, 0x05010000, 0xADBB091D, 0x01000000, 0xAEC21F20, 0x05010000, 0xB203091D, 0x01000000, 0xB3091F20, 0x00000000, 0xB66C2020, 0x05010000, 0xB9B1091D, 0x05000000, 0xBAB71820, 0x05010000, 0xBD46091D, 0x05010000, 0xBD46091D, 0x05010000, 0xBD46091D, 0x05010000, 0xBD46091D, 0x05010000, 0xBD46091D, 0x05000000, 0xBE4F1720, 0x05010000, 0x3876091D, 0x05010000, 0x3876091D, 0x05010000, 0x3876091D, 0x05010000, 0x3876091D, 0x05010000, 0x3876091D, 0x05010000, 0x3876091D, 0x05010000, 0x3876091D, 0x05010000, 0x3876091D, 0x00400000, 0x00510047)
ep_assert(len(GrpWire32) == len(GrpWire64) == (131 + 1) * 2)

"""
Wirefram.grp
"""
Wirefram32 = (0x000D0040, 0x07263F28, 0x02070000, 0x0E473C2E, 0x06000000, 0x138F3540, 0x00050000, 0x19A54037, 0x05010000, 0x21A4091D, 0x00010000, 0x22AE403F, 0x05010000, 0x2B47091D, 0x00050000, 0x2C464039, 0x07000000, 0x34AF3440, 0x00000000, 0x3C654040, 0x00060000, 0x45FC4030, 0x02000000, 0x4E013C40, 0x01000000, 0x569D3840, 0x06010000, 0x5F51353F, 0x05010000, 0x6560091D, 0x030D0000, 0x66613C23, 0x01070000, 0x6B223F2E, 0x00050000, 0x709D4037, 0x05010000, 0x789C091D, 0x06000000, 0x138F3540, 0x000D0000, 0x79A03F28, 0x07000000, 0x80BB3440, 0x00000000, 0x3C654040, 0x00010000, 0x8871403F, 0x05010000, 0x9106091D, 0x00000000, 0x9204403C, 0x05010000, 0x9B81091D, 0x05010000, 0x9B81091D, 0x01000000, 0x9C843840, 0x01000000, 0x9C843840, 0x00000000, 0xA53A403C, 0x05010000, 0xAEBB091D, 0x00060000, 0xAFC54030, 0x000D0000, 0xB7CA3F28, 0x000C0000, 0xBEED402E, 0x080A0000, 0xC72D2D2A, 0x0B070000, 0xCA632732, 0x000B0000, 0xCE713F2E, 0x050B0000, 0xD383352F, 0x06000000, 0xD7A73440, 0x05030000, 0xDCBF3A35, 0x0C050000, 0xE2062E36, 0x01070000, 0xE7093D31, 0x07020000, 0xEE803139, 0x08000000, 0xF35C3140, 0x06040000, 0xF8A03537, 0x06010000, 0xFEB7323F, 0x04010000, 0x0259393E, 0x06000001, 0xD7A73440, 0x06040000, 0xF8A03537, 0x01090000, 0x07D43A2F, 0x00000001, 0x0E943D37, 0x06010001, 0xFEB7323F, 0x050B0000, 0xD383352F, 0x000B0000, 0xCE713F2E, 0x07020000, 0xEE803139, 0x08000000, 0xF35C3140, 0x01070000, 0xE7093D31, 0x03000000, 0x14913B40, 0x0F0B0001, 0x1C6D282D, 0x04020001, 0x20DB363A, 0x00000001, 0x2736403D, 0x01000001, 0x2E773D3C, 0x00030001, 0x35F7403C, 0x01030001, 0x3EE23E3A, 0x00010001, 0x45F3403E, 0x01070001, 0x50023E31, 0x00000001, 0x57B34040, 0x03010001, 0x61413D3C, 0x03000001, 0x6A5E3840, 0x02000001, 0x723C3D40, 0x00000001, 0x79784040, 0x00010001, 0x826D403F, 0x05000001, 0x8C203340, 0x00000001, 0x2736403D, 0x00000001, 0x2736403D, 0x03010001, 0x61413D3C, 0x00010001, 0x928E403E, 0x01070001, 0x50023E31, 0x00000001, 0x57B34040, 0x02000001, 0x9C9E3D40, 0x06030001, 0xA3D9383A, 0x00010001, 0xAAF4403F, 0x06030001, 0xB4A7383A, 0x04050001, 0xBBC23635, 0x05010001, 0xC1EC091D, 0x00000001, 0xC2ED4040, 0x05010001, 0xCBE4091D, 0x02000001, 0xCCE03D40, 0x06010001, 0xD41B373F, 0x09000001, 0xDC072F3E, 0x06000001, 0xE03E3340, 0x03000001, 0xE8683B40, 0x00030001, 0xF0814036, 0x01000001, 0xF6393E40, 0x0A000001, 0xFB052B40, 0x0A020001, 0x005C3433, 0x10050002, 0x05911C35, 0x00000002, 0x2736403D, 0x02070001, 0x0E473C2E, 0x02070000, 0x0E473C2E, 0x05010000, 0x08D0091D, 0x01000002, 0x09D13840, 0x06000002, 0x12873440, 0x02080002, 0x0E473C2E, 0x05010000, 0x08D0091D, 0x03000002, 0x18343A40, 0x01000002, 0x219E3F40, 0x00000002, 0x29F84040, 0x06000002, 0x336D3540, 0x06000002, 0x3B713540, 0x02000002, 0x442A3D40, 0x00000002, 0x4E4A3F40, 0x00000002, 0x57703F40, 0x00000002, 0x625C4040, 0x00000002, 0x6BFB3F40, 0x09000002, 0x75BB3140, 0x04000002, 0x7D793640, 0x00000002, 0x85254040, 0x05010002, 0x8DFE091D, 0x01010002, 0x8F023D3C, 0x01000002, 0x97DE3F40, 0x09000002, 0xA1902E40, 0x00000002, 0xA76B4040, 0x00070002, 0xB20C4032, 0x0B000002, 0xBACA2B40, 0x07000002, 0xC1C93240, 0x0E040002, 0xC8422633, 0x070D0002, 0xCBBA3423, 0x070D0002, 0xCBBA3423, 0x04000002, 0xCEBA3340, 0x0B030002, 0xD7C2353A, 0x00000002, 0xDE8C4040, 0x00020002, 0xE78C403D, 0x00000002, 0xF0A53F40, 0x01000002, 0xFA143E40, 0x06010002, 0x033F303F, 0x00080003, 0x098F4032, 0x01000003, 0x11D7393E, 0x01000003, 0x19C13C3F, 0x01000003, 0x22463C40, 0x00070003, 0x2AE14032, 0x0A000003, 0x32EF2C40, 0x08010003, 0x3984363D, 0x00020003, 0x41D3403D, 0x05010003, 0x4A20091D, 0x06000003, 0x4B2A2E40, 0x06000003, 0x511F3240, 0x0A000003, 0x5A152E40, 0x01020003, 0x60EB3B3C, 0x01010003, 0x69103B3E, 0x0A000003, 0x6EC12A40, 0x0A000003, 0x6EC12A40, 0x05010003, 0x7590091D, 0x00000003, 0x769A4040, 0x00000003, 0x81AB4040, 0x00030003, 0x8AE8403A, 0x05000003, 0x94893540, 0x05010003, 0x9C57091D, 0x04000003, 0x9D573740, 0x02000003, 0xA5F23C40, 0x05010003, 0xAFB8091D, 0x0B000003, 0xB0BF2D40, 0x00000003, 0xB6F54040, 0x00000003, 0xC1264040, 0x00000003, 0xCB334040, 0x00000003, 0xD3114040, 0x00000003, 0xDCA33F40, 0x00000003, 0xE4A14040, 0x07000003, 0xEDA53340, 0x04000003, 0xF52B3840, 0x02000003, 0xFD4F3C40, 0x0A000003, 0x06A72D40, 0x00000004, 0x0DEF3F40, 0x06000004, 0x15EC3240, 0x00050004, 0x1DB34037, 0x07000004, 0x252A3540, 0x07000004, 0x252A3540, 0x07000004, 0x252A3540, 0x1A140004, 0x2E0A0717, 0x1A140004, 0x2E0A0717, 0x1D0D0004, 0x2E7D0725, 0x05010004, 0x2F46091D, 0x1F080004, 0x3050082D, 0x05010004, 0x2F46091D, 0x1F080004, 0x313F0836, 0x05020004, 0x324C353D, 0x00000004, 0x38833F40, 0x0C000004, 0x40812A40, 0x00050004, 0x47294034, 0x00000004, 0x4E8D3F40, 0x05010004, 0x2F46091D, 0x05010004, 0x2F46091D, 0x05010004, 0x2F46091D, 0x0F000004, 0x57F42340, 0x08000004, 0x5D122C40, 0x07010004, 0x61AB293F, 0x0F000004, 0x65E72340, 0x08000004, 0x5D122C40, 0x07010004, 0x61AB293F, 0x06000004, 0x6B053640, 0x10010004, 0x7221243E, 0x05010004, 0x7590091D, 0x0B000003, 0x779D2C40, 0x05010004, 0x7590091D, 0x05010003, 0x7590091D, 0x05010003, 0x7590091D, 0x05010003, 0x7590091D, 0x05010003, 0x7590091D, 0x090B0003, 0x7C802E2B, 0x0D0E0004, 0x80692725, 0x0A120004, 0x84402D1C, 0x0D0E0004, 0x80692725, 0x0A120004, 0x84402D1C, 0x05010004, 0x2F46091D, 0x02080004, 0x87653D2D, 0x04100004, 0x8B623323, 0x070A0004, 0x8F66322D, 0x11040004, 0x94592239, 0x070D0004, 0xCBBA3423, 0x00000002, 0x97804040, 0x00000004, 0x97804040, 0x06070004, 0x9F033633, 0x06070004, 0x9F033633, 0x05070004, 0xA2D23734, 0x05070004, 0xA2D23734, 0x03060004, 0xAA223B33, 0x03060004, 0xAA223B33, 0x007E0004, 0x008C0082)
Wirefram64 = (0x000D0040, 0x0AB63F28, 0x02070000, 0x11D73C2E, 0x06000000, 0x171F3540, 0x00050000, 0x1D354037, 0x05010000, 0x2534091D, 0x00010000, 0x263E403F, 0x05010000, 0x2ED7091D, 0x00050000, 0x2FD64039, 0x07000000, 0x383F3440, 0x00000000, 0x3FF54040, 0x00060000, 0x498C4030, 0x02000000, 0x51913C40, 0x01000000, 0x5A2D3840, 0x06010000, 0x62E1353F, 0x05010000, 0x68F0091D, 0x030D0000, 0x69F13C23, 0x01070000, 0x6EB23F2E, 0x00050000, 0x742D4037, 0x05010000, 0x7C2C091D, 0x06000000, 0x171F3540, 0x000D0000, 0x7D303F28, 0x07000000, 0x844B3440, 0x00000000, 0x3FF54040, 0x00010000, 0x8C01403F, 0x05010000, 0x9496091D, 0x00000000, 0x9594403C, 0x05010000, 0x9F11091D, 0x05010000, 0x9F11091D, 0x01000000, 0xA0143840, 0x01000000, 0xA0143840, 0x00000000, 0xA8CA403C, 0x05010000, 0xB24B091D, 0x00060000, 0xB3554030, 0x000D0000, 0xBB5A3F28, 0x000C0000, 0xC27D402E, 0x080A0000, 0xCABD2D2A, 0x0B070000, 0xCDF32732, 0x000B0000, 0xD2013F2E, 0x050B0000, 0xD713352F, 0x06000000, 0xDB373440, 0x05030000, 0xE04F3A35, 0x0C050000, 0xE5962E36, 0x01070000, 0xEA993D31, 0x07020000, 0xF2103139, 0x08000000, 0xF6EC3140, 0x06040000, 0xFC303537, 0x06010000, 0x0247323F, 0x04010001, 0x05E9393E, 0x06000001, 0xDB373440, 0x06040000, 0xFC303537, 0x01090000, 0x0B643A2F, 0x00000001, 0x12243D37, 0x06010001, 0x0247323F, 0x050B0001, 0xD713352F, 0x000B0000, 0xD2013F2E, 0x07020000, 0xF2103139, 0x08000000, 0xF6EC3140, 0x01070000, 0xEA993D31, 0x03000000, 0x18213B40, 0x0F0B0001, 0x1FFD282D, 0x04020001, 0x246B363A, 0x00000001, 0x2AC6403D, 0x01000001, 0x32073D3C, 0x00030001, 0x3987403C, 0x01030001, 0x42723E3A, 0x00010001, 0x4983403E, 0x01070001, 0x53923E31, 0x00000001, 0x5B434040, 0x03010001, 0x64D13D3C, 0x03000001, 0x6DEE3840, 0x02000001, 0x75CC3D40, 0x00000001, 0x7D084040, 0x00010001, 0x85FD403F, 0x05000001, 0x8FB03340, 0x00000001, 0x2AC6403D, 0x00000001, 0x2AC6403D, 0x03010001, 0x64D13D3C, 0x00010001, 0x961E403E, 0x01070001, 0x53923E31, 0x00000001, 0x5B434040, 0x02000001, 0xA02E3D40, 0x06030001, 0xA769383A, 0x00010001, 0xAE84403F, 0x06030001, 0xB837383A, 0x04050001, 0xBF523635, 0x05010001, 0xC57C091D, 0x00000001, 0xC67D4040, 0x05010001, 0xCF74091D, 0x02000001, 0xD0703D40, 0x06010001, 0xD7AB373F, 0x09000001, 0xDF972F3E, 0x06000001, 0xE3CE3340, 0x03000001, 0xEBF83B40, 0x00030001, 0xF4114036, 0x01000001, 0xF9C93E40, 0x0A000001, 0xFE952B40, 0x0A020001, 0x03EC3433, 0x10050002, 0x09211C35, 0x00000002, 0x2AC6403D, 0x02070001, 0x11D73C2E, 0x02070000, 0x11D73C2E, 0x05010000, 0x0C60091D, 0x01000002, 0x0D613840, 0x06000002, 0x16173440, 0x02080002, 0x11D73C2E, 0x05010000, 0x0C60091D, 0x03000002, 0x1BC43A40, 0x01000002, 0x252E3F40, 0x00000002, 0x2D884040, 0x06000002, 0x36FD3540, 0x06000002, 0x3F013540, 0x02000002, 0x47BA3D40, 0x00000002, 0x51DA3F40, 0x00000002, 0x5B003F40, 0x00000002, 0x65EC4040, 0x00000002, 0x6F8B3F40, 0x09000002, 0x794B3140, 0x04000002, 0x81093640, 0x00000002, 0x88B54040, 0x05010002, 0x918E091D, 0x01010002, 0x92923D3C, 0x01000002, 0x9B6E3F40, 0x09000002, 0xA5202E40, 0x00000002, 0xAAFB4040, 0x00070002, 0xB59C4032, 0x0B000002, 0xBE5A2B40, 0x07000002, 0xC5593240, 0x0E040002, 0xCBD22633, 0x070D0002, 0xCF4A3423, 0x070D0002, 0xCF4A3423, 0x04000002, 0xD24A3340, 0x0B030002, 0xDB52353A, 0x00000002, 0xE21C4040, 0x00020002, 0xEB1C403D, 0x00000002, 0xF4353F40, 0x01000002, 0xFDA43E40, 0x06010002, 0x06CF303F, 0x00080003, 0x0D1F4032, 0x01000003, 0x1567393E, 0x01000003, 0x1D513C3F, 0x01000003, 0x25D63C40, 0x00070003, 0x2E714032, 0x0A000003, 0x367F2C40, 0x08010003, 0x3D14363D, 0x00020003, 0x4563403D, 0x05010003, 0x4DB0091D, 0x06000003, 0x4EBA2E40, 0x06000003, 0x54AF3240, 0x0A000003, 0x5DA52E40, 0x01020003, 0x647B3B3C, 0x01010003, 0x6CA03B3E, 0x0A000003, 0x72512A40, 0x0A000003, 0x72512A40, 0x05010003, 0x7920091D, 0x00000003, 0x7A2A4040, 0x00000003, 0x853B4040, 0x00030003, 0x8E78403A, 0x05000003, 0x98193540, 0x05010003, 0x9FE7091D, 0x04000003, 0xA0E73740, 0x02000003, 0xA9823C40, 0x05010003, 0xB348091D, 0x0B000003, 0xB44F2D40, 0x00000003, 0xBA854040, 0x00000003, 0xC4B64040, 0x00000003, 0xCEC34040, 0x00000003, 0xD6A14040, 0x00000003, 0xE0333F40, 0x00000003, 0xE8314040, 0x07000003, 0xF1353340, 0x04000003, 0xF8BB3840, 0x02000003, 0x00DF3C40, 0x0A000004, 0x0A372D40, 0x00000004, 0x117F3F40, 0x06000004, 0x197C3240, 0x00050004, 0x21434037, 0x07000004, 0x28BA3540, 0x07000004, 0x28BA3540, 0x07000004, 0x28BA3540, 0x1A140004, 0x319A0717, 0x1A140004, 0x319A0717, 0x1D0D0004, 0x320D0725, 0x05010004, 0x32D6091D, 0x1F080004, 0x33E0082D, 0x05010004, 0x32D6091D, 0x1F080004, 0x34CF0836, 0x05020004, 0x35DC353D, 0x00000004, 0x3C133F40, 0x0C000004, 0x44112A40, 0x00050004, 0x4AB94034, 0x00000004, 0x521D3F40, 0x05010004, 0x32D6091D, 0x05010004, 0x32D6091D, 0x05010004, 0x32D6091D, 0x0F000004, 0x5B842340, 0x08000004, 0x60A22C40, 0x07010004, 0x653B293F, 0x0F000004, 0x69772340, 0x08000004, 0x60A22C40, 0x07010004, 0x653B293F, 0x06000004, 0x6E953640, 0x10010004, 0x75B1243E, 0x05010004, 0x7920091D, 0x0B000003, 0x7B2D2C40, 0x05010004, 0x7920091D, 0x05010003, 0x7920091D, 0x05010003, 0x7920091D, 0x05010003, 0x7920091D, 0x05010003, 0x7920091D, 0x090B0003, 0x80102E2B, 0x0D0E0004, 0x83F92725, 0x0A120004, 0x87D02D1C, 0x0D0E0004, 0x83F92725, 0x0A120004, 0x87D02D1C, 0x05010004, 0x32D6091D, 0x02080004, 0x8AF53D2D, 0x04100004, 0x8EF23323, 0x070A0004, 0x92F6322D, 0x11040004, 0x97E92239, 0x070D0004, 0xCF4A3423, 0x00000002, 0x9B104040, 0x00000004, 0x9B104040, 0x06070004, 0xA2933633, 0x06070004, 0xA2933633, 0x05070004, 0xA6623734, 0x05070004, 0xA6623734, 0x03060004, 0xADB23B33, 0x03060004, 0xADB23B33, 0x007E0004, 0x008C0082)
ep_assert(len(Wirefram32) == len(Wirefram64) == (228 + 1) * 2)
# fmt: on
