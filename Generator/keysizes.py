# Schema
# { 
#     "keysize": unit or string ID (string IDs must be handled via custom code; numerical units will be auto-calculated),
#     "stabilizer_dist": X distance of one of the stabilizer holes (or leftside if stabilizer_dist_right is defined),
#     "stabilizer_dist_right": X distance of the right stabilizer holes,
#     "stabilizer_vert": Whether or not to rotate the stabilizers vertically
# }

KEYSIZES_MX = [
    {
        "keysize": 1
    },
    {
        "keysize": 1.25
    },
    {
        "keysize": 1.5
    },
    {
        "keysize": 1.75
    },
    {
        "keysize": 2,
        "stabilizer_dist": 11.938
    },
    {
        "keysize": 2.25,
        "stabilizer_dist": 11.938
    },
    {
        "keysize": 2.75,
        "stabilizer_dist": 11.938
    },
    {
        "keysize": 3,
        "stabilizer_dist": 19.05
    },
    {
        "keysize": 6,
        "stabilizer_dist": 47.625
    },
    {
        "keysize": 6.25,
        "stabilizer_dist": 50
    },
    {
        "keysize": 6.5,
        "stabilizer_dist": 50
    },
    {
        "keysize": 7,
        "stabilizer_dist": 57.15
    },
    {
        "keysize": 8,
        "stabilizer_dist": 66.675
    },
    {
        "keysize": 9,
        "stabilizer_dist": 66.675
    },
    {
        "keysize": 10,
        "stabilizer_dist": 66.675
    },
    {
        "keysize": "ISO",
        "stabilizer_vert": True,
        "stabilizer_dist": 11.938
    },
    {
        "keysize": "ISO-Rotated",
        "stabilizer_dist": 11.938
    },
    {
        "keysize": "6U-Offcenter",
        "stabilizer_dist": 57.15,
        "stabilizer_dist_right": 38.1
    },
    {
        "keysize": "2U-Vertical",
        "stabilizer_vert": True,
        "stabilizer_dist": 11.938
    }
]

KEYSIZES_ALPS = [
    {"keysize": 1},
    {"keysize": 1.25},
    {"keysize": 1.5},
    {"keysize": 1.75},
    {"keysize": 2},
    {"keysize": 2.25},
    {"keysize": 2.75},
    {"keysize": 3},
    {"keysize": 6.25},
    {"keysize": 6.5},
    {"keysize": 7},
    {"keysize": "ISO"}
]

KEYSIZES_MX_ALPS = KEYSIZES_MX[:] + [
    {"keysize": 6.5}
]
