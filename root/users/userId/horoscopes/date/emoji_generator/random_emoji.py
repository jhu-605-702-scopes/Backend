import random

smileys = [
  {
      "code": "U+1F600",
      "name": "grinning face",
      "image": "😀",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F603",
      "name": "grinning face with big eyes",
      "image": "😃",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F604",
      "name": "grinning face with smiling eyes",
      "image": "😄",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F601",
      "name": "beaming face with smiling eyes",
      "image": "😁",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F606",
      "name": "grinning squinting face",
      "image": "😆",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F605",
      "name": "grinning face with sweat",
      "image": "😅",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F923",
      "name": "rolling on the floor laughing",
      "image": "🤣",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F602",
      "name": "face with tears of joy",
      "image": "😂",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F642",
      "name": "slightly smiling face",
      "image": "🙂",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F643",
      "name": "upside-down face",
      "image": "🙃",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1FAE0",
      "name": "melting face",
      "image": "🫠",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F609",
      "name": "winking face",
      "image": "😉",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F60A",
      "name": "smiling face with smiling eyes",
      "image": "😊",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F607",
      "name": "smiling face with halo",
      "image": "😇",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F970",
      "name": "smiling face with hearts",
      "image": "🥰",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F60D",
      "name": "smiling face with heart-eyes",
      "image": "😍",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F929",
      "name": "star-struck",
      "image": "🤩",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F618",
      "name": "face blowing a kiss",
      "image": "😘",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F617",
      "name": "kissing face",
      "image": "😗",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+263A",
      "name": "smiling face",
      "image": "☺",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F61A",
      "name": "kissing face with closed eyes",
      "image": "😚",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F619",
      "name": "kissing face with smiling eyes",
      "image": "😙",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F972",
      "name": "smiling face with tear",
      "image": "🥲",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F60B",
      "name": "face savoring food",
      "image": "😋",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F61B",
      "name": "face with tongue",
      "image": "😛",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F61C",
      "name": "winking face with tongue",
      "image": "😜",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F92A",
      "name": "zany face",
      "image": "🤪",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F61D",
      "name": "squinting face with tongue",
      "image": "😝",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F911",
      "name": "money-mouth face",
      "image": "🤑",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F917",
      "name": "smiling face with open hands",
      "image": "🤗",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F92D",
      "name": "face with hand over mouth",
      "image": "🤭",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1FAE2",
      "name": "face with open eyes and hand over mouth",
      "image": "🫢",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1FAE3",
      "name": "face with peeking eye",
      "image": "🫣",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F92B",
      "name": "shushing face",
      "image": "🤫",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F914",
      "name": "thinking face",
      "image": "🤔",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1FAE1",
      "name": "saluting face",
      "image": "🫡",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F910",
      "name": "zipper-mouth face",
      "image": "🤐",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F928",
      "name": "face with raised eyebrow",
      "image": "🤨",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F610",
      "name": "neutral face",
      "image": "😐",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F611",
      "name": "expressionless face",
      "image": "😑",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F636",
      "name": "face without mouth",
      "image": "😶",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1FAE5",
      "name": "dotted line face",
      "image": "🫥",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F636 U+200D U+1F32B U+FE0F",
      "name": "face in clouds",
      "image": "😶‍🌫️",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F60F",
      "name": "smirking face",
      "image": "😏",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F612",
      "name": "unamused face",
      "image": "😒",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F644",
      "name": "face with rolling eyes",
      "image": "🙄",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F62C",
      "name": "grimacing face",
      "image": "😬",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F62E U+200D U+1F4A8",
      "name": "face exhaling",
      "image": "😮‍💨",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F925",
      "name": "lying face",
      "image": "🤥",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F60C",
      "name": "relieved face",
      "image": "😌",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F614",
      "name": "pensive face",
      "image": "😔",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F62A",
      "name": "sleepy face",
      "image": "😪",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F924",
      "name": "drooling face",
      "image": "🤤",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F634",
      "name": "sleeping face",
      "image": "😴",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F637",
      "name": "face with medical mask",
      "image": "😷",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F912",
      "name": "face with thermometer",
      "image": "🤒",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F915",
      "name": "face with head-bandage",
      "image": "🤕",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F922",
      "name": "nauseated face",
      "image": "🤢",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F92E",
      "name": "face vomiting",
      "image": "🤮",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F927",
      "name": "sneezing face",
      "image": "🤧",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F975",
      "name": "hot face",
      "image": "🥵",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F976",
      "name": "cold face",
      "image": "🥶",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F974",
      "name": "woozy face",
      "image": "🥴",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F635",
      "name": "face with crossed-out eyes",
      "image": "😵",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F635 U+200D U+1F4AB",
      "name": "face with spiral eyes",
      "image": "😵‍💫",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F92F",
      "name": "exploding head",
      "image": "🤯",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F920",
      "name": "cowboy hat face",
      "image": "🤠",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F973",
      "name": "partying face",
      "image": "🥳",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F978",
      "name": "disguised face",
      "image": "🥸",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F60E",
      "name": "smiling face with sunglasses",
      "image": "😎",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F913",
      "name": "nerd face",
      "image": "🤓",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F9D0",
      "name": "face with monocle",
      "image": "🧐",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F615",
      "name": "confused face",
      "image": "😕",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1FAE4",
      "name": "face with diagonal mouth",
      "image": "🫤",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F61F",
      "name": "worried face",
      "image": "😟",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F641",
      "name": "slightly frowning face",
      "image": "🙁",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+2639",
      "name": "frowning face",
      "image": "☹",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F62E",
      "name": "face with open mouth",
      "image": "😮",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F62F",
      "name": "hushed face",
      "image": "😯",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F632",
      "name": "astonished face",
      "image": "😲",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F633",
      "name": "flushed face",
      "image": "😳",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F97A",
      "name": "pleading face",
      "image": "🥺",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F979",
      "name": "face holding back tears",
      "image": "🥹",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F626",
      "name": "frowning face with open mouth",
      "image": "😦",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F627",
      "name": "anguished face",
      "image": "😧",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F628",
      "name": "fearful face",
      "image": "😨",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F630",
      "name": "anxious face with sweat",
      "image": "😰",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F625",
      "name": "sad but relieved face",
      "image": "😥",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F622",
      "name": "crying face",
      "image": "😢",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F62D",
      "name": "loudly crying face",
      "image": "😭",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F631",
      "name": "face screaming in fear",
      "image": "😱",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F616",
      "name": "confounded face",
      "image": "😖",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F623",
      "name": "persevering face",
      "image": "😣",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F61E",
      "name": "disappointed face",
      "image": "😞",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F613",
      "name": "downcast face with sweat",
      "image": "😓",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F629",
      "name": "weary face",
      "image": "😩",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F62B",
      "name": "tired face",
      "image": "😫",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F971",
      "name": "yawning face",
      "image": "🥱",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F624",
      "name": "face with steam from nose",
      "image": "😤",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F621",
      "name": "enraged face",
      "image": "😡",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F620",
      "name": "angry face",
      "image": "😠",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F92C",
      "name": "face with symbols on mouth",
      "image": "🤬",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F608",
      "name": "smiling face with horns",
      "image": "😈",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F47F",
      "name": "angry face with horns",
      "image": "👿",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F480",
      "name": "skull",
      "image": "💀",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+2620",
      "name": "skull and crossbones",
      "image": "☠",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F4A9",
      "name": "pile of poo",
      "image": "💩",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F921",
      "name": "clown face",
      "image": "🤡",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F479",
      "name": "ogre",
      "image": "👹",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F47A",
      "name": "goblin",
      "image": "👺",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F47B",
      "name": "ghost",
      "image": "👻",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F47D",
      "name": "alien",
      "image": "👽",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F47E",
      "name": "alien monster",
      "image": "👾",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F916",
      "name": "robot",
      "image": "🤖",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F63A",
      "name": "grinning cat",
      "image": "😺",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F638",
      "name": "grinning cat with smiling eyes",
      "image": "😸",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F639",
      "name": "cat with tears of joy",
      "image": "😹",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F63B",
      "name": "smiling cat with heart-eyes",
      "image": "😻",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F63C",
      "name": "cat with wry smile",
      "image": "😼",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F63D",
      "name": "kissing cat",
      "image": "😽",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F640",
      "name": "weary cat",
      "image": "🙀",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F63F",
      "name": "crying cat",
      "image": "😿",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F63E",
      "name": "pouting cat",
      "image": "😾",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F648",
      "name": "see-no-evil monkey",
      "image": "🙈",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F649",
      "name": "hear-no-evil monkey",
      "image": "🙉",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F64A",
      "name": "speak-no-evil monkey",
      "image": "🙊",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F48C",
      "name": "love letter",
      "image": "💌",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F498",
      "name": "heart with arrow",
      "image": "💘",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F49D",
      "name": "heart with ribbon",
      "image": "💝",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F496",
      "name": "sparkling heart",
      "image": "💖",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F497",
      "name": "growing heart",
      "image": "💗",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F493",
      "name": "beating heart",
      "image": "💓",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F49E",
      "name": "revolving hearts",
      "image": "💞",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F495",
      "name": "two hearts",
      "image": "💕",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F49F",
      "name": "heart decoration",
      "image": "💟",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+2763",
      "name": "heart exclamation",
      "image": "❣",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F494",
      "name": "broken heart",
      "image": "💔",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+2764 U+FE0F U+200D U+1F525",
      "name": "heart on fire",
      "image": "❤️‍🔥",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+2764 U+FE0F U+200D U+1FA79",
      "name": "mending heart",
      "image": "❤️‍🩹",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+2764",
      "name": "red heart",
      "image": "❤",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F9E1",
      "name": "orange heart",
      "image": "🧡",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F49B",
      "name": "yellow heart",
      "image": "💛",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F49A",
      "name": "green heart",
      "image": "💚",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F499",
      "name": "blue heart",
      "image": "💙",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F49C",
      "name": "purple heart",
      "image": "💜",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F90E",
      "name": "brown heart",
      "image": "🤎",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F5A4",
      "name": "black heart",
      "image": "🖤",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F90D",
      "name": "white heart",
      "image": "🤍",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F48B",
      "name": "kiss mark",
      "image": "💋",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F4AF",
      "name": "hundred points",
      "image": "💯",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F4A2",
      "name": "anger symbol",
      "image": "💢",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F4A5",
      "name": "collision",
      "image": "💥",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F4AB",
      "name": "dizzy",
      "image": "💫",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F4A6",
      "name": "sweat droplets",
      "image": "💦",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F4A8",
      "name": "dashing away",
      "image": "💨",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F573",
      "name": "hole",
      "image": "🕳",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F4AC",
      "name": "speech balloon",
      "image": "💬",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F441 U+FE0F U+200D U+1F5E8 U+FE0F",
      "name": "eye in speech bubble",
      "image": "👁️‍🗨️",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F5E8",
      "name": "left speech bubble",
      "image": "🗨",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F5EF",
      "name": "right anger bubble",
      "image": "🗯",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F4AD",
      "name": "thought balloon",
      "image": "💭",
      "category": "Smileys & Emotion"
    },
    {
      "code": "U+1F4A4",
      "name": "ZZZ",
      "image": "💤",
      "category": "Smileys & Emotion"
    },{
      "code": "U+1F44B",
      "name": "waving hand",
      "image": "👋",
      "category": "People & Body"
    },
    {
      "code": "U+1F91A",
      "name": "raised back of hand",
      "image": "🤚",
      "category": "People & Body"
    },
    {
      "code": "U+1F590",
      "name": "hand with fingers splayed",
      "image": "🖐",
      "category": "People & Body"
    },
    {
      "code": "U+270B",
      "name": "raised hand",
      "image": "✋",
      "category": "People & Body"
    },
    {
      "code": "U+1F596",
      "name": "vulcan salute",
      "image": "🖖",
      "category": "People & Body"
    },
    {
      "code": "U+1FAF1",
      "name": "rightwards hand",
      "image": "🫱",
      "category": "People & Body"
    },
    {
      "code": "U+1FAF2",
      "name": "leftwards hand",
      "image": "🫲",
      "category": "People & Body"
    },
    {
      "code": "U+1FAF3",
      "name": "palm down hand",
      "image": "🫳",
      "category": "People & Body"
    },
    {
      "code": "U+1FAF4",
      "name": "palm up hand",
      "image": "🫴",
      "category": "People & Body"
    },
    {
      "code": "U+1F44C",
      "name": "OK hand",
      "image": "👌",
      "category": "People & Body"
    },
    {
      "code": "U+1F90C",
      "name": "pinched fingers",
      "image": "🤌",
      "category": "People & Body"
    },
    {
      "code": "U+1F90F",
      "name": "pinching hand",
      "image": "🤏",
      "category": "People & Body"
    },
    {
      "code": "U+270C",
      "name": "victory hand",
      "image": "✌",
      "category": "People & Body"
    },
    {
      "code": "U+1F91E",
      "name": "crossed fingers",
      "image": "🤞",
      "category": "People & Body"
    },
    {
      "code": "U+1FAF0",
      "name": "hand with index finger and thumb crossed",
      "image": "🫰",
      "category": "People & Body"
    },
    {
      "code": "U+1F91F",
      "name": "love-you gesture",
      "image": "🤟",
      "category": "People & Body"
    },
    {
      "code": "U+1F918",
      "name": "sign of the horns",
      "image": "🤘",
      "category": "People & Body"
    },
    {
      "code": "U+1F919",
      "name": "call me hand",
      "image": "🤙",
      "category": "People & Body"
    },
    {
      "code": "U+1F448",
      "name": "backhand index pointing left",
      "image": "👈",
      "category": "People & Body"
    },
    {
      "code": "U+1F449",
      "name": "backhand index pointing right",
      "image": "👉",
      "category": "People & Body"
    },
    {
      "code": "U+1F446",
      "name": "backhand index pointing up",
      "image": "👆",
      "category": "People & Body"
    },
    {
      "code": "U+1F595",
      "name": "middle finger",
      "image": "🖕",
      "category": "People & Body"
    },
    {
      "code": "U+1F447",
      "name": "backhand index pointing down",
      "image": "👇",
      "category": "People & Body"
    },
    {
      "code": "U+261D",
      "name": "index pointing up",
      "image": "☝",
      "category": "People & Body"
    },
    {
      "code": "U+1FAF5",
      "name": "index pointing at the viewer",
      "image": "🫵",
      "category": "People & Body"
    },
    {
      "code": "U+1F44D",
      "name": "thumbs up",
      "image": "👍",
      "category": "People & Body"
    },
    {
      "code": "U+1F44E",
      "name": "thumbs down",
      "image": "👎",
      "category": "People & Body"
    },
    {
      "code": "U+270A",
      "name": "raised fist",
      "image": "✊",
      "category": "People & Body"
    },
    {
      "code": "U+1F44A",
      "name": "oncoming fist",
      "image": "👊",
      "category": "People & Body"
    },
    {
      "code": "U+1F91B",
      "name": "left-facing fist",
      "image": "🤛",
      "category": "People & Body"
    },
    {
      "code": "U+1F91C",
      "name": "right-facing fist",
      "image": "🤜",
      "category": "People & Body"
    },
    {
      "code": "U+1F44F",
      "name": "clapping hands",
      "image": "👏",
      "category": "People & Body"
    },
    {
      "code": "U+1F64C",
      "name": "raising hands",
      "image": "🙌",
      "category": "People & Body"
    },
    {
      "code": "U+1FAF6",
      "name": "heart hands",
      "image": "🫶",
      "category": "People & Body"
    },
    {
      "code": "U+1F450",
      "name": "open hands",
      "image": "👐",
      "category": "People & Body"
    },
    {
      "code": "U+1F932",
      "name": "palms up together",
      "image": "🤲",
      "category": "People & Body"
    },
    {
      "code": "U+1F91D",
      "name": "handshake",
      "image": "🤝",
      "category": "People & Body"
    },
    {
      "code": "U+1F64F",
      "name": "folded hands",
      "image": "🙏",
      "category": "People & Body"
    },
    {
      "code": "U+270D",
      "name": "writing hand",
      "image": "✍",
      "category": "People & Body"
    },
    {
      "code": "U+1F485",
      "name": "nail polish",
      "image": "💅",
      "category": "People & Body"
    },
    {
      "code": "U+1F933",
      "name": "selfie",
      "image": "🤳",
      "category": "People & Body"
    },
    {
      "code": "U+1F4AA",
      "name": "flexed biceps",
      "image": "💪",
      "category": "People & Body"
    },
    {
      "code": "U+1F9BE",
      "name": "mechanical arm",
      "image": "🦾",
      "category": "People & Body"
    },
    {
      "code": "U+1F9BF",
      "name": "mechanical leg",
      "image": "🦿",
      "category": "People & Body"
    },
    {
      "code": "U+1F9B5",
      "name": "leg",
      "image": "🦵",
      "category": "People & Body"
    },
    {
      "code": "U+1F9B6",
      "name": "foot",
      "image": "🦶",
      "category": "People & Body"
    },
    {
      "code": "U+1F442",
      "name": "ear",
      "image": "👂",
      "category": "People & Body"
    },
    {
      "code": "U+1F9BB",
      "name": "ear with hearing aid",
      "image": "🦻",
      "category": "People & Body"
    },
    {
      "code": "U+1F443",
      "name": "nose",
      "image": "👃",
      "category": "People & Body"
    },
    {
      "code": "U+1F9E0",
      "name": "brain",
      "image": "🧠",
      "category": "People & Body"
    },
    {
      "code": "U+1FAC0",
      "name": "anatomical heart",
      "image": "🫀",
      "category": "People & Body"
    },
    {
      "code": "U+1FAC1",
      "name": "lungs",
      "image": "🫁",
      "category": "People & Body"
    },
    {
      "code": "U+1F9B7",
      "name": "tooth",
      "image": "🦷",
      "category": "People & Body"
    },
    {
      "code": "U+1F9B4",
      "name": "bone",
      "image": "🦴",
      "category": "People & Body"
    },
    {
      "code": "U+1F440",
      "name": "eyes",
      "image": "👀",
      "category": "People & Body"
    },
    {
      "code": "U+1F441",
      "name": "eye",
      "image": "👁",
      "category": "People & Body"
    },
    {
      "code": "U+1F445",
      "name": "tongue",
      "image": "👅",
      "category": "People & Body"
    },
    {
      "code": "U+1F444",
      "name": "mouth",
      "image": "👄",
      "category": "People & Body"
    },
    {
      "code": "U+1FAE6",
      "name": "biting lip",
      "image": "🫦",
      "category": "People & Body"
    },
    {
      "code": "U+1F476",
      "name": "baby",
      "image": "👶",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D2",
      "name": "child",
      "image": "🧒",
      "category": "People & Body"
    },
    {
      "code": "U+1F466",
      "name": "boy",
      "image": "👦",
      "category": "People & Body"
    },
    {
      "code": "U+1F467",
      "name": "girl",
      "image": "👧",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D1",
      "name": "person",
      "image": "🧑",
      "category": "People & Body"
    },
    {
      "code": "U+1F471",
      "name": "person: blond hair",
      "image": "👱",
      "category": "People & Body"
    },
    {
      "code": "U+1F468",
      "name": "man",
      "image": "👨",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D4",
      "name": "person: beard",
      "image": "🧔",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D4 U+200D U+2642 U+FE0F",
      "name": "man: beard",
      "image": "🧔‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D4 U+200D U+2640 U+FE0F",
      "name": "woman: beard",
      "image": "🧔‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F9B0",
      "name": "man: red hair",
      "image": "👨‍🦰",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F9B1",
      "name": "man: curly hair",
      "image": "👨‍🦱",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F9B3",
      "name": "man: white hair",
      "image": "👨‍🦳",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F9B2",
      "name": "man: bald",
      "image": "👨‍🦲",
      "category": "People & Body"
    },
    {
      "code": "U+1F469",
      "name": "woman",
      "image": "👩",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F9B0",
      "name": "woman: red hair",
      "image": "👩‍🦰",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D1 U+200D U+1F9B0",
      "name": "person: red hair",
      "image": "🧑‍🦰",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F9B1",
      "name": "woman: curly hair",
      "image": "👩‍🦱",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D1 U+200D U+1F9B1",
      "name": "person: curly hair",
      "image": "🧑‍🦱",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F9B3",
      "name": "woman: white hair",
      "image": "👩‍🦳",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D1 U+200D U+1F9B3",
      "name": "person: white hair",
      "image": "🧑‍🦳",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F9B2",
      "name": "woman: bald",
      "image": "👩‍🦲",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D1 U+200D U+1F9B2",
      "name": "person: bald",
      "image": "🧑‍🦲",
      "category": "People & Body"
    },
    {
      "code": "U+1F471 U+200D U+2640 U+FE0F",
      "name": "woman: blond hair",
      "image": "👱‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F471 U+200D U+2642 U+FE0F",
      "name": "man: blond hair",
      "image": "👱‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D3",
      "name": "older person",
      "image": "🧓",
      "category": "People & Body"
    },
    {
      "code": "U+1F474",
      "name": "old man",
      "image": "👴",
      "category": "People & Body"
    },
    {
      "code": "U+1F475",
      "name": "old woman",
      "image": "👵",
      "category": "People & Body"
    },
    {
      "code": "U+1F64D",
      "name": "person frowning",
      "image": "🙍",
      "category": "People & Body"
    },
    {
      "code": "U+1F64D U+200D U+2642 U+FE0F",
      "name": "man frowning",
      "image": "🙍‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F64D U+200D U+2640 U+FE0F",
      "name": "woman frowning",
      "image": "🙍‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F64E",
      "name": "person pouting",
      "image": "🙎",
      "category": "People & Body"
    },
    {
      "code": "U+1F64E U+200D U+2642 U+FE0F",
      "name": "man pouting",
      "image": "🙎‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F64E U+200D U+2640 U+FE0F",
      "name": "woman pouting",
      "image": "🙎‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F645",
      "name": "person gesturing NO",
      "image": "🙅",
      "category": "People & Body"
    },
    {
      "code": "U+1F645 U+200D U+2642 U+FE0F",
      "name": "man gesturing NO",
      "image": "🙅‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F645 U+200D U+2640 U+FE0F",
      "name": "woman gesturing NO",
      "image": "🙅‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F646",
      "name": "person gesturing OK",
      "image": "🙆",
      "category": "People & Body"
    },
    {
      "code": "U+1F646 U+200D U+2642 U+FE0F",
      "name": "man gesturing OK",
      "image": "🙆‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F646 U+200D U+2640 U+FE0F",
      "name": "woman gesturing OK",
      "image": "🙆‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F481",
      "name": "person tipping hand",
      "image": "💁",
      "category": "People & Body"
    },
    {
      "code": "U+1F481 U+200D U+2642 U+FE0F",
      "name": "man tipping hand",
      "image": "💁‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F481 U+200D U+2640 U+FE0F",
      "name": "woman tipping hand",
      "image": "💁‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F64B",
      "name": "person raising hand",
      "image": "🙋",
      "category": "People & Body"
    },
    {
      "code": "U+1F64B U+200D U+2642 U+FE0F",
      "name": "man raising hand",
      "image": "🙋‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F64B U+200D U+2640 U+FE0F",
      "name": "woman raising hand",
      "image": "🙋‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9CF",
      "name": "deaf person",
      "image": "🧏",
      "category": "People & Body"
    },
    {
      "code": "U+1F9CF U+200D U+2642 U+FE0F",
      "name": "deaf man",
      "image": "🧏‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9CF U+200D U+2640 U+FE0F",
      "name": "deaf woman",
      "image": "🧏‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F647",
      "name": "person bowing",
      "image": "🙇",
      "category": "People & Body"
    },
    {
      "code": "U+1F647 U+200D U+2642 U+FE0F",
      "name": "man bowing",
      "image": "🙇‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F647 U+200D U+2640 U+FE0F",
      "name": "woman bowing",
      "image": "🙇‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F926",
      "name": "person facepalming",
      "image": "🤦",
      "category": "People & Body"
    },
    {
      "code": "U+1F926 U+200D U+2642 U+FE0F",
      "name": "man facepalming",
      "image": "🤦‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F926 U+200D U+2640 U+FE0F",
      "name": "woman facepalming",
      "image": "🤦‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F937",
      "name": "person shrugging",
      "image": "🤷",
      "category": "People & Body"
    },
    {
      "code": "U+1F937 U+200D U+2642 U+FE0F",
      "name": "man shrugging",
      "image": "🤷‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F937 U+200D U+2640 U+FE0F",
      "name": "woman shrugging",
      "image": "🤷‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D1 U+200D U+2695 U+FE0F",
      "name": "health worker",
      "image": "🧑‍⚕️",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+2695 U+FE0F",
      "name": "man health worker",
      "image": "👨‍⚕️",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+2695 U+FE0F",
      "name": "woman health worker",
      "image": "👩‍⚕️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D1 U+200D U+1F393",
      "name": "student",
      "image": "🧑‍🎓",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F393",
      "name": "man student",
      "image": "👨‍🎓",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F393",
      "name": "woman student",
      "image": "👩‍🎓",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D1 U+200D U+1F3EB",
      "name": "teacher",
      "image": "🧑‍🏫",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F3EB",
      "name": "man teacher",
      "image": "👨‍🏫",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F3EB",
      "name": "woman teacher",
      "image": "👩‍🏫",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D1 U+200D U+2696 U+FE0F",
      "name": "judge",
      "image": "🧑‍⚖️",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+2696 U+FE0F",
      "name": "man judge",
      "image": "👨‍⚖️",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+2696 U+FE0F",
      "name": "woman judge",
      "image": "👩‍⚖️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D1 U+200D U+1F33E",
      "name": "farmer",
      "image": "🧑‍🌾",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F33E",
      "name": "man farmer",
      "image": "👨‍🌾",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F33E",
      "name": "woman farmer",
      "image": "👩‍🌾",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D1 U+200D U+1F373",
      "name": "cook",
      "image": "🧑‍🍳",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F373",
      "name": "man cook",
      "image": "👨‍🍳",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F373",
      "name": "woman cook",
      "image": "👩‍🍳",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D1 U+200D U+1F527",
      "name": "mechanic",
      "image": "🧑‍🔧",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F527",
      "name": "man mechanic",
      "image": "👨‍🔧",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F527",
      "name": "woman mechanic",
      "image": "👩‍🔧",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D1 U+200D U+1F3ED",
      "name": "factory worker",
      "image": "🧑‍🏭",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F3ED",
      "name": "man factory worker",
      "image": "👨‍🏭",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F3ED",
      "name": "woman factory worker",
      "image": "👩‍🏭",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D1 U+200D U+1F4BC",
      "name": "office worker",
      "image": "🧑‍💼",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F4BC",
      "name": "man office worker",
      "image": "👨‍💼",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F4BC",
      "name": "woman office worker",
      "image": "👩‍💼",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D1 U+200D U+1F52C",
      "name": "scientist",
      "image": "🧑‍🔬",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F52C",
      "name": "man scientist",
      "image": "👨‍🔬",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F52C",
      "name": "woman scientist",
      "image": "👩‍🔬",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D1 U+200D U+1F4BB",
      "name": "technologist",
      "image": "🧑‍💻",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F4BB",
      "name": "man technologist",
      "image": "👨‍💻",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F4BB",
      "name": "woman technologist",
      "image": "👩‍💻",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D1 U+200D U+1F3A4",
      "name": "singer",
      "image": "🧑‍🎤",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F3A4",
      "name": "man singer",
      "image": "👨‍🎤",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F3A4",
      "name": "woman singer",
      "image": "👩‍🎤",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D1 U+200D U+1F3A8",
      "name": "artist",
      "image": "🧑‍🎨",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F3A8",
      "name": "man artist",
      "image": "👨‍🎨",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F3A8",
      "name": "woman artist",
      "image": "👩‍🎨",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D1 U+200D U+2708 U+FE0F",
      "name": "pilot",
      "image": "🧑‍✈️",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+2708 U+FE0F",
      "name": "man pilot",
      "image": "👨‍✈️",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+2708 U+FE0F",
      "name": "woman pilot",
      "image": "👩‍✈️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D1 U+200D U+1F680",
      "name": "astronaut",
      "image": "🧑‍🚀",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F680",
      "name": "man astronaut",
      "image": "👨‍🚀",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F680",
      "name": "woman astronaut",
      "image": "👩‍🚀",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D1 U+200D U+1F692",
      "name": "firefighter",
      "image": "🧑‍🚒",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F692",
      "name": "man firefighter",
      "image": "👨‍🚒",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F692",
      "name": "woman firefighter",
      "image": "👩‍🚒",
      "category": "People & Body"
    },
    {
      "code": "U+1F46E",
      "name": "police officer",
      "image": "👮",
      "category": "People & Body"
    },
    {
      "code": "U+1F46E U+200D U+2642 U+FE0F",
      "name": "man police officer",
      "image": "👮‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F46E U+200D U+2640 U+FE0F",
      "name": "woman police officer",
      "image": "👮‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F575",
      "name": "detective",
      "image": "🕵",
      "category": "People & Body"
    },
    {
      "code": "U+1F575 U+FE0F U+200D U+2642 U+FE0F",
      "name": "man detective",
      "image": "🕵️‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F575 U+FE0F U+200D U+2640 U+FE0F",
      "name": "woman detective",
      "image": "🕵️‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F482",
      "name": "guard",
      "image": "💂",
      "category": "People & Body"
    },
    {
      "code": "U+1F482 U+200D U+2642 U+FE0F",
      "name": "man guard",
      "image": "💂‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F482 U+200D U+2640 U+FE0F",
      "name": "woman guard",
      "image": "💂‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F977",
      "name": "ninja",
      "image": "🥷",
      "category": "People & Body"
    },
    {
      "code": "U+1F477",
      "name": "construction worker",
      "image": "👷",
      "category": "People & Body"
    },
    {
      "code": "U+1F477 U+200D U+2642 U+FE0F",
      "name": "man construction worker",
      "image": "👷‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F477 U+200D U+2640 U+FE0F",
      "name": "woman construction worker",
      "image": "👷‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1FAC5",
      "name": "person with crown",
      "image": "🫅",
      "category": "People & Body"
    },
    {
      "code": "U+1F934",
      "name": "prince",
      "image": "🤴",
      "category": "People & Body"
    },
    {
      "code": "U+1F478",
      "name": "princess",
      "image": "👸",
      "category": "People & Body"
    },
    {
      "code": "U+1F473",
      "name": "person wearing turban",
      "image": "👳",
      "category": "People & Body"
    },
    {
      "code": "U+1F473 U+200D U+2642 U+FE0F",
      "name": "man wearing turban",
      "image": "👳‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F473 U+200D U+2640 U+FE0F",
      "name": "woman wearing turban",
      "image": "👳‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F472",
      "name": "person with skullcap",
      "image": "👲",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D5",
      "name": "woman with headscarf",
      "image": "🧕",
      "category": "People & Body"
    },
    {
      "code": "U+1F935",
      "name": "person in tuxedo",
      "image": "🤵",
      "category": "People & Body"
    },
    {
      "code": "U+1F935 U+200D U+2642 U+FE0F",
      "name": "man in tuxedo",
      "image": "🤵‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F935 U+200D U+2640 U+FE0F",
      "name": "woman in tuxedo",
      "image": "🤵‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F470",
      "name": "person with veil",
      "image": "👰",
      "category": "People & Body"
    },
    {
      "code": "U+1F470 U+200D U+2642 U+FE0F",
      "name": "man with veil",
      "image": "👰‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F470 U+200D U+2640 U+FE0F",
      "name": "woman with veil",
      "image": "👰‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F930",
      "name": "pregnant woman",
      "image": "🤰",
      "category": "People & Body"
    },
    {
      "code": "U+1FAC3",
      "name": "pregnant man",
      "image": "🫃",
      "category": "People & Body"
    },
    {
      "code": "U+1FAC4",
      "name": "pregnant person",
      "image": "🫄",
      "category": "People & Body"
    },
    {
      "code": "U+1F931",
      "name": "breast-feeding",
      "image": "🤱",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F37C",
      "name": "woman feeding baby",
      "image": "👩‍🍼",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F37C",
      "name": "man feeding baby",
      "image": "👨‍🍼",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D1 U+200D U+1F37C",
      "name": "person feeding baby",
      "image": "🧑‍🍼",
      "category": "People & Body"
    },
    {
      "code": "U+1F47C",
      "name": "baby angel",
      "image": "👼",
      "category": "People & Body"
    },
    {
      "code": "U+1F385",
      "name": "Santa Claus",
      "image": "🎅",
      "category": "People & Body"
    },
    {
      "code": "U+1F936",
      "name": "Mrs. Claus",
      "image": "🤶",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D1 U+200D U+1F384",
      "name": "mx claus",
      "image": "🧑‍🎄",
      "category": "People & Body"
    },
    {
      "code": "U+1F9B8",
      "name": "superhero",
      "image": "🦸",
      "category": "People & Body"
    },
    {
      "code": "U+1F9B8 U+200D U+2642 U+FE0F",
      "name": "man superhero",
      "image": "🦸‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9B8 U+200D U+2640 U+FE0F",
      "name": "woman superhero",
      "image": "🦸‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9B9",
      "name": "supervillain",
      "image": "🦹",
      "category": "People & Body"
    },
    {
      "code": "U+1F9B9 U+200D U+2642 U+FE0F",
      "name": "man supervillain",
      "image": "🦹‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9B9 U+200D U+2640 U+FE0F",
      "name": "woman supervillain",
      "image": "🦹‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D9",
      "name": "mage",
      "image": "🧙",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D9 U+200D U+2642 U+FE0F",
      "name": "man mage",
      "image": "🧙‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D9 U+200D U+2640 U+FE0F",
      "name": "woman mage",
      "image": "🧙‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9DA",
      "name": "fairy",
      "image": "🧚",
      "category": "People & Body"
    },
    {
      "code": "U+1F9DA U+200D U+2642 U+FE0F",
      "name": "man fairy",
      "image": "🧚‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9DA U+200D U+2640 U+FE0F",
      "name": "woman fairy",
      "image": "🧚‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9DB",
      "name": "vampire",
      "image": "🧛",
      "category": "People & Body"
    },
    {
      "code": "U+1F9DB U+200D U+2642 U+FE0F",
      "name": "man vampire",
      "image": "🧛‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9DB U+200D U+2640 U+FE0F",
      "name": "woman vampire",
      "image": "🧛‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9DC",
      "name": "merperson",
      "image": "🧜",
      "category": "People & Body"
    },
    {
      "code": "U+1F9DC U+200D U+2642 U+FE0F",
      "name": "merman",
      "image": "🧜‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9DC U+200D U+2640 U+FE0F",
      "name": "mermaid",
      "image": "🧜‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9DD",
      "name": "elf",
      "image": "🧝",
      "category": "People & Body"
    },
    {
      "code": "U+1F9DD U+200D U+2642 U+FE0F",
      "name": "man elf",
      "image": "🧝‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9DD U+200D U+2640 U+FE0F",
      "name": "woman elf",
      "image": "🧝‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9DE",
      "name": "genie",
      "image": "🧞",
      "category": "People & Body"
    },
    {
      "code": "U+1F9DE U+200D U+2642 U+FE0F",
      "name": "man genie",
      "image": "🧞‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9DE U+200D U+2640 U+FE0F",
      "name": "woman genie",
      "image": "🧞‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9DF",
      "name": "zombie",
      "image": "🧟",
      "category": "People & Body"
    },
    {
      "code": "U+1F9DF U+200D U+2642 U+FE0F",
      "name": "man zombie",
      "image": "🧟‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9DF U+200D U+2640 U+FE0F",
      "name": "woman zombie",
      "image": "🧟‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9CC",
      "name": "troll",
      "image": "🧌",
      "category": "People & Body"
    },
    {
      "code": "U+1F486",
      "name": "person getting massage",
      "image": "💆",
      "category": "People & Body"
    },
    {
      "code": "U+1F486 U+200D U+2642 U+FE0F",
      "name": "man getting massage",
      "image": "💆‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F486 U+200D U+2640 U+FE0F",
      "name": "woman getting massage",
      "image": "💆‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F487",
      "name": "person getting haircut",
      "image": "💇",
      "category": "People & Body"
    },
    {
      "code": "U+1F487 U+200D U+2642 U+FE0F",
      "name": "man getting haircut",
      "image": "💇‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F487 U+200D U+2640 U+FE0F",
      "name": "woman getting haircut",
      "image": "💇‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F6B6",
      "name": "person walking",
      "image": "🚶",
      "category": "People & Body"
    },
    {
      "code": "U+1F6B6 U+200D U+2642 U+FE0F",
      "name": "man walking",
      "image": "🚶‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F6B6 U+200D U+2640 U+FE0F",
      "name": "woman walking",
      "image": "🚶‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9CD",
      "name": "person standing",
      "image": "🧍",
      "category": "People & Body"
    },
    {
      "code": "U+1F9CD U+200D U+2642 U+FE0F",
      "name": "man standing",
      "image": "🧍‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9CD U+200D U+2640 U+FE0F",
      "name": "woman standing",
      "image": "🧍‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9CE",
      "name": "person kneeling",
      "image": "🧎",
      "category": "People & Body"
    },
    {
      "code": "U+1F9CE U+200D U+2642 U+FE0F",
      "name": "man kneeling",
      "image": "🧎‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9CE U+200D U+2640 U+FE0F",
      "name": "woman kneeling",
      "image": "🧎‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D1 U+200D U+1F9AF",
      "name": "person with white cane",
      "image": "🧑‍🦯",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F9AF",
      "name": "man with white cane",
      "image": "👨‍🦯",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F9AF",
      "name": "woman with white cane",
      "image": "👩‍🦯",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D1 U+200D U+1F9BC",
      "name": "person in motorized wheelchair",
      "image": "🧑‍🦼",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F9BC",
      "name": "man in motorized wheelchair",
      "image": "👨‍🦼",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F9BC",
      "name": "woman in motorized wheelchair",
      "image": "👩‍🦼",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D1 U+200D U+1F9BD",
      "name": "person in manual wheelchair",
      "image": "🧑‍🦽",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F9BD",
      "name": "man in manual wheelchair",
      "image": "👨‍🦽",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F9BD",
      "name": "woman in manual wheelchair",
      "image": "👩‍🦽",
      "category": "People & Body"
    },
    {
      "code": "U+1F3C3",
      "name": "person running",
      "image": "🏃",
      "category": "People & Body"
    },
    {
      "code": "U+1F3C3 U+200D U+2642 U+FE0F",
      "name": "man running",
      "image": "🏃‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F3C3 U+200D U+2640 U+FE0F",
      "name": "woman running",
      "image": "🏃‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F483",
      "name": "woman dancing",
      "image": "💃",
      "category": "People & Body"
    },
    {
      "code": "U+1F57A",
      "name": "man dancing",
      "image": "🕺",
      "category": "People & Body"
    },
    {
      "code": "U+1F574",
      "name": "person in suit levitating",
      "image": "🕴",
      "category": "People & Body"
    },
    {
      "code": "U+1F46F",
      "name": "people with bunny ears",
      "image": "👯",
      "category": "People & Body"
    },
    {
      "code": "U+1F46F U+200D U+2642 U+FE0F",
      "name": "men with bunny ears",
      "image": "👯‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F46F U+200D U+2640 U+FE0F",
      "name": "women with bunny ears",
      "image": "👯‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D6",
      "name": "person in steamy room",
      "image": "🧖",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D6 U+200D U+2642 U+FE0F",
      "name": "man in steamy room",
      "image": "🧖‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D6 U+200D U+2640 U+FE0F",
      "name": "woman in steamy room",
      "image": "🧖‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D7",
      "name": "person climbing",
      "image": "🧗",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D7 U+200D U+2642 U+FE0F",
      "name": "man climbing",
      "image": "🧗‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D7 U+200D U+2640 U+FE0F",
      "name": "woman climbing",
      "image": "🧗‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F93A",
      "name": "person fencing",
      "image": "🤺",
      "category": "People & Body"
    },
    {
      "code": "U+1F3C7",
      "name": "horse racing",
      "image": "🏇",
      "category": "People & Body"
    },
    {
      "code": "U+26F7",
      "name": "skier",
      "image": "⛷",
      "category": "People & Body"
    },
    {
      "code": "U+1F3C2",
      "name": "snowboarder",
      "image": "🏂",
      "category": "People & Body"
    },
    {
      "code": "U+1F3CC",
      "name": "person golfing",
      "image": "🏌",
      "category": "People & Body"
    },
    {
      "code": "U+1F3CC U+FE0F U+200D U+2642 U+FE0F",
      "name": "man golfing",
      "image": "🏌️‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F3CC U+FE0F U+200D U+2640 U+FE0F",
      "name": "woman golfing",
      "image": "🏌️‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F3C4",
      "name": "person surfing",
      "image": "🏄",
      "category": "People & Body"
    },
    {
      "code": "U+1F3C4 U+200D U+2642 U+FE0F",
      "name": "man surfing",
      "image": "🏄‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F3C4 U+200D U+2640 U+FE0F",
      "name": "woman surfing",
      "image": "🏄‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F6A3",
      "name": "person rowing boat",
      "image": "🚣",
      "category": "People & Body"
    },
    {
      "code": "U+1F6A3 U+200D U+2642 U+FE0F",
      "name": "man rowing boat",
      "image": "🚣‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F6A3 U+200D U+2640 U+FE0F",
      "name": "woman rowing boat",
      "image": "🚣‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F3CA",
      "name": "person swimming",
      "image": "🏊",
      "category": "People & Body"
    },
    {
      "code": "U+1F3CA U+200D U+2642 U+FE0F",
      "name": "man swimming",
      "image": "🏊‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F3CA U+200D U+2640 U+FE0F",
      "name": "woman swimming",
      "image": "🏊‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+26F9",
      "name": "person bouncing ball",
      "image": "⛹",
      "category": "People & Body"
    },
    {
      "code": "U+26F9 U+FE0F U+200D U+2642 U+FE0F",
      "name": "man bouncing ball",
      "image": "⛹️‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+26F9 U+FE0F U+200D U+2640 U+FE0F",
      "name": "woman bouncing ball",
      "image": "⛹️‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F3CB",
      "name": "person lifting weights",
      "image": "🏋",
      "category": "People & Body"
    },
    {
      "code": "U+1F3CB U+FE0F U+200D U+2642 U+FE0F",
      "name": "man lifting weights",
      "image": "🏋️‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F3CB U+FE0F U+200D U+2640 U+FE0F",
      "name": "woman lifting weights",
      "image": "🏋️‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F6B4",
      "name": "person biking",
      "image": "🚴",
      "category": "People & Body"
    },
    {
      "code": "U+1F6B4 U+200D U+2642 U+FE0F",
      "name": "man biking",
      "image": "🚴‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F6B4 U+200D U+2640 U+FE0F",
      "name": "woman biking",
      "image": "🚴‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F6B5",
      "name": "person mountain biking",
      "image": "🚵",
      "category": "People & Body"
    },
    {
      "code": "U+1F6B5 U+200D U+2642 U+FE0F",
      "name": "man mountain biking",
      "image": "🚵‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F6B5 U+200D U+2640 U+FE0F",
      "name": "woman mountain biking",
      "image": "🚵‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F938",
      "name": "person cartwheeling",
      "image": "🤸",
      "category": "People & Body"
    },
    {
      "code": "U+1F938 U+200D U+2642 U+FE0F",
      "name": "man cartwheeling",
      "image": "🤸‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F938 U+200D U+2640 U+FE0F",
      "name": "woman cartwheeling",
      "image": "🤸‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F93C",
      "name": "people wrestling",
      "image": "🤼",
      "category": "People & Body"
    },
    {
      "code": "U+1F93C U+200D U+2642 U+FE0F",
      "name": "men wrestling",
      "image": "🤼‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F93C U+200D U+2640 U+FE0F",
      "name": "women wrestling",
      "image": "🤼‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F93D",
      "name": "person playing water polo",
      "image": "🤽",
      "category": "People & Body"
    },
    {
      "code": "U+1F93D U+200D U+2642 U+FE0F",
      "name": "man playing water polo",
      "image": "🤽‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F93D U+200D U+2640 U+FE0F",
      "name": "woman playing water polo",
      "image": "🤽‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F93E",
      "name": "person playing handball",
      "image": "🤾",
      "category": "People & Body"
    },
    {
      "code": "U+1F93E U+200D U+2642 U+FE0F",
      "name": "man playing handball",
      "image": "🤾‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F93E U+200D U+2640 U+FE0F",
      "name": "woman playing handball",
      "image": "🤾‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F939",
      "name": "person juggling",
      "image": "🤹",
      "category": "People & Body"
    },
    {
      "code": "U+1F939 U+200D U+2642 U+FE0F",
      "name": "man juggling",
      "image": "🤹‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F939 U+200D U+2640 U+FE0F",
      "name": "woman juggling",
      "image": "🤹‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D8",
      "name": "person in lotus position",
      "image": "🧘",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D8 U+200D U+2642 U+FE0F",
      "name": "man in lotus position",
      "image": "🧘‍♂️",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D8 U+200D U+2640 U+FE0F",
      "name": "woman in lotus position",
      "image": "🧘‍♀️",
      "category": "People & Body"
    },
    {
      "code": "U+1F6C0",
      "name": "person taking bath",
      "image": "🛀",
      "category": "People & Body"
    },
    {
      "code": "U+1F6CC",
      "name": "person in bed",
      "image": "🛌",
      "category": "People & Body"
    },
    {
      "code": "U+1F9D1 U+200D U+1F91D U+200D U+1F9D1",
      "name": "people holding hands",
      "image": "🧑‍🤝‍🧑",
      "category": "People & Body"
    },
    {
      "code": "U+1F46D",
      "name": "women holding hands",
      "image": "👭",
      "category": "People & Body"
    },
    {
      "code": "U+1F46B",
      "name": "woman and man holding hands",
      "image": "👫",
      "category": "People & Body"
    },
    {
      "code": "U+1F46C",
      "name": "men holding hands",
      "image": "👬",
      "category": "People & Body"
    },
    {
      "code": "U+1F48F",
      "name": "kiss",
      "image": "💏",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+2764 U+FE0F U+200D U+1F48B U+200D U+1F468",
      "name": "kiss: woman, man",
      "image": "👩‍❤️‍💋‍👨",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+2764 U+FE0F U+200D U+1F48B U+200D U+1F468",
      "name": "kiss: man, man",
      "image": "👨‍❤️‍💋‍👨",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+2764 U+FE0F U+200D U+1F48B U+200D U+1F469",
      "name": "kiss: woman, woman",
      "image": "👩‍❤️‍💋‍👩",
      "category": "People & Body"
    },
    {
      "code": "U+1F491",
      "name": "couple with heart",
      "image": "💑",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+2764 U+FE0F U+200D U+1F468",
      "name": "couple with heart: woman, man",
      "image": "👩‍❤️‍👨",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+2764 U+FE0F U+200D U+1F468",
      "name": "couple with heart: man, man",
      "image": "👨‍❤️‍👨",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+2764 U+FE0F U+200D U+1F469",
      "name": "couple with heart: woman, woman",
      "image": "👩‍❤️‍👩",
      "category": "People & Body"
    },
    {
      "code": "U+1F46A",
      "name": "family",
      "image": "👪",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F469 U+200D U+1F466",
      "name": "family: man, woman, boy",
      "image": "👨‍👩‍👦",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F469 U+200D U+1F467",
      "name": "family: man, woman, girl",
      "image": "👨‍👩‍👧",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F469 U+200D U+1F467 U+200D U+1F466",
      "name": "family: man, woman, girl, boy",
      "image": "👨‍👩‍👧‍👦",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F469 U+200D U+1F466 U+200D U+1F466",
      "name": "family: man, woman, boy, boy",
      "image": "👨‍👩‍👦‍👦",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F469 U+200D U+1F467 U+200D U+1F467",
      "name": "family: man, woman, girl, girl",
      "image": "👨‍👩‍👧‍👧",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F468 U+200D U+1F466",
      "name": "family: man, man, boy",
      "image": "👨‍👨‍👦",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F468 U+200D U+1F467",
      "name": "family: man, man, girl",
      "image": "👨‍👨‍👧",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F468 U+200D U+1F467 U+200D U+1F466",
      "name": "family: man, man, girl, boy",
      "image": "👨‍👨‍👧‍👦",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F468 U+200D U+1F466 U+200D U+1F466",
      "name": "family: man, man, boy, boy",
      "image": "👨‍👨‍👦‍👦",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F468 U+200D U+1F467 U+200D U+1F467",
      "name": "family: man, man, girl, girl",
      "image": "👨‍👨‍👧‍👧",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F469 U+200D U+1F466",
      "name": "family: woman, woman, boy",
      "image": "👩‍👩‍👦",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F469 U+200D U+1F467",
      "name": "family: woman, woman, girl",
      "image": "👩‍👩‍👧",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F469 U+200D U+1F467 U+200D U+1F466",
      "name": "family: woman, woman, girl, boy",
      "image": "👩‍👩‍👧‍👦",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F469 U+200D U+1F466 U+200D U+1F466",
      "name": "family: woman, woman, boy, boy",
      "image": "👩‍👩‍👦‍👦",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F469 U+200D U+1F467 U+200D U+1F467",
      "name": "family: woman, woman, girl, girl",
      "image": "👩‍👩‍👧‍👧",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F466",
      "name": "family: man, boy",
      "image": "👨‍👦",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F466 U+200D U+1F466",
      "name": "family: man, boy, boy",
      "image": "👨‍👦‍👦",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F467",
      "name": "family: man, girl",
      "image": "👨‍👧",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F467 U+200D U+1F466",
      "name": "family: man, girl, boy",
      "image": "👨‍👧‍👦",
      "category": "People & Body"
    },
    {
      "code": "U+1F468 U+200D U+1F467 U+200D U+1F467",
      "name": "family: man, girl, girl",
      "image": "👨‍👧‍👧",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F466",
      "name": "family: woman, boy",
      "image": "👩‍👦",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F466 U+200D U+1F466",
      "name": "family: woman, boy, boy",
      "image": "👩‍👦‍👦",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F467",
      "name": "family: woman, girl",
      "image": "👩‍👧",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F467 U+200D U+1F466",
      "name": "family: woman, girl, boy",
      "image": "👩‍👧‍👦",
      "category": "People & Body"
    },
    {
      "code": "U+1F469 U+200D U+1F467 U+200D U+1F467",
      "name": "family: woman, girl, girl",
      "image": "👩‍👧‍👧",
      "category": "People & Body"
    },
    {
      "code": "U+1F5E3",
      "name": "speaking head",
      "image": "🗣",
      "category": "People & Body"
    },
    {
      "code": "U+1F464",
      "name": "bust in silhouette",
      "image": "👤",
      "category": "People & Body"
    },
    {
      "code": "U+1F465",
      "name": "busts in silhouette",
      "image": "👥",
      "category": "People & Body"
    },
    {
      "code": "U+1FAC2",
      "name": "people hugging",
      "image": "🫂",
      "category": "People & Body"
    },
    {
      "code": "U+1F463",
      "name": "footprints",
      "image": "👣",
      "category": "People & Body"
    },
    {
      "code": "U+1F9B0",
      "name": "red hair",
      "image": "🦰",
      "category": "People & Body"
    },
    {
      "code": "U+1F9B1",
      "name": "curly hair",
      "image": "🦱",
      "category": "People & Body"
    },
    {
      "code": "U+1F9B3",
      "name": "white hair",
      "image": "🦳",
      "category": "People & Body"
    },
    {
      "code": "U+1F9B2",
      "name": "bald",
      "image": "🦲",
      "category": "People & Body"
    },
    {
      "code": "U+1F435",
      "name": "monkey face",
      "image": "🐵",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F412",
      "name": "monkey",
      "image": "🐒",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F98D",
      "name": "gorilla",
      "image": "🦍",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F9A7",
      "name": "orangutan",
      "image": "🦧",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F436",
      "name": "dog face",
      "image": "🐶",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F415",
      "name": "dog",
      "image": "🐕",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F9AE",
      "name": "guide dog",
      "image": "🦮",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F415 U+200D U+1F9BA",
      "name": "service dog",
      "image": "🐕‍🦺",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F429",
      "name": "poodle",
      "image": "🐩",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F43A",
      "name": "wolf",
      "image": "🐺",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F98A",
      "name": "fox",
      "image": "🦊",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F99D",
      "name": "raccoon",
      "image": "🦝",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F431",
      "name": "cat face",
      "image": "🐱",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F408",
      "name": "cat",
      "image": "🐈",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F408 U+200D U+2B1B",
      "name": "black cat",
      "image": "🐈‍⬛",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F981",
      "name": "lion",
      "image": "🦁",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F42F",
      "name": "tiger face",
      "image": "🐯",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F405",
      "name": "tiger",
      "image": "🐅",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F406",
      "name": "leopard",
      "image": "🐆",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F434",
      "name": "horse face",
      "image": "🐴",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F40E",
      "name": "horse",
      "image": "🐎",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F984",
      "name": "unicorn",
      "image": "🦄",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F993",
      "name": "zebra",
      "image": "🦓",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F98C",
      "name": "deer",
      "image": "🦌",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F9AC",
      "name": "bison",
      "image": "🦬",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F42E",
      "name": "cow face",
      "image": "🐮",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F402",
      "name": "ox",
      "image": "🐂",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F403",
      "name": "water buffalo",
      "image": "🐃",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F404",
      "name": "cow",
      "image": "🐄",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F437",
      "name": "pig face",
      "image": "🐷",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F416",
      "name": "pig",
      "image": "🐖",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F417",
      "name": "boar",
      "image": "🐗",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F43D",
      "name": "pig nose",
      "image": "🐽",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F40F",
      "name": "ram",
      "image": "🐏",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F411",
      "name": "ewe",
      "image": "🐑",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F410",
      "name": "goat",
      "image": "🐐",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F42A",
      "name": "camel",
      "image": "🐪",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F42B",
      "name": "two-hump camel",
      "image": "🐫",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F999",
      "name": "llama",
      "image": "🦙",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F992",
      "name": "giraffe",
      "image": "🦒",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F418",
      "name": "elephant",
      "image": "🐘",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F9A3",
      "name": "mammoth",
      "image": "🦣",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F98F",
      "name": "rhinoceros",
      "image": "🦏",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F99B",
      "name": "hippopotamus",
      "image": "🦛",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F42D",
      "name": "mouse face",
      "image": "🐭",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F401",
      "name": "mouse",
      "image": "🐁",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F400",
      "name": "rat",
      "image": "🐀",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F439",
      "name": "hamster",
      "image": "🐹",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F430",
      "name": "rabbit face",
      "image": "🐰",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F407",
      "name": "rabbit",
      "image": "🐇",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F43F",
      "name": "chipmunk",
      "image": "🐿",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F9AB",
      "name": "beaver",
      "image": "🦫",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F994",
      "name": "hedgehog",
      "image": "🦔",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F987",
      "name": "bat",
      "image": "🦇",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F43B",
      "name": "bear",
      "image": "🐻",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F43B U+200D U+2744 U+FE0F",
      "name": "polar bear",
      "image": "🐻‍❄️",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F428",
      "name": "koala",
      "image": "🐨",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F43C",
      "name": "panda",
      "image": "🐼",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F9A5",
      "name": "sloth",
      "image": "🦥",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F9A6",
      "name": "otter",
      "image": "🦦",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F9A8",
      "name": "skunk",
      "image": "🦨",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F998",
      "name": "kangaroo",
      "image": "🦘",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F9A1",
      "name": "badger",
      "image": "🦡",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F43E",
      "name": "paw prints",
      "image": "🐾",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F983",
      "name": "turkey",
      "image": "🦃",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F414",
      "name": "chicken",
      "image": "🐔",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F413",
      "name": "rooster",
      "image": "🐓",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F423",
      "name": "hatching chick",
      "image": "🐣",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F424",
      "name": "baby chick",
      "image": "🐤",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F425",
      "name": "front-facing baby chick",
      "image": "🐥",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F426",
      "name": "bird",
      "image": "🐦",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F427",
      "name": "penguin",
      "image": "🐧",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F54A",
      "name": "dove",
      "image": "🕊",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F985",
      "name": "eagle",
      "image": "🦅",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F986",
      "name": "duck",
      "image": "🦆",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F9A2",
      "name": "swan",
      "image": "🦢",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F989",
      "name": "owl",
      "image": "🦉",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F9A4",
      "name": "dodo",
      "image": "🦤",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1FAB6",
      "name": "feather",
      "image": "🪶",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F9A9",
      "name": "flamingo",
      "image": "🦩",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F99A",
      "name": "peacock",
      "image": "🦚",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F99C",
      "name": "parrot",
      "image": "🦜",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F438",
      "name": "frog",
      "image": "🐸",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F40A",
      "name": "crocodile",
      "image": "🐊",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F422",
      "name": "turtle",
      "image": "🐢",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F98E",
      "name": "lizard",
      "image": "🦎",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F40D",
      "name": "snake",
      "image": "🐍",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F432",
      "name": "dragon face",
      "image": "🐲",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F409",
      "name": "dragon",
      "image": "🐉",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F995",
      "name": "sauropod",
      "image": "🦕",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F996",
      "name": "T-Rex",
      "image": "🦖",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F433",
      "name": "spouting whale",
      "image": "🐳",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F40B",
      "name": "whale",
      "image": "🐋",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F42C",
      "name": "dolphin",
      "image": "🐬",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F9AD",
      "name": "seal",
      "image": "🦭",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F41F",
      "name": "fish",
      "image": "🐟",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F420",
      "name": "tropical fish",
      "image": "🐠",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F421",
      "name": "blowfish",
      "image": "🐡",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F988",
      "name": "shark",
      "image": "🦈",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F419",
      "name": "octopus",
      "image": "🐙",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F41A",
      "name": "spiral shell",
      "image": "🐚",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1FAB8",
      "name": "coral",
      "image": "🪸",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F40C",
      "name": "snail",
      "image": "🐌",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F98B",
      "name": "butterfly",
      "image": "🦋",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F41B",
      "name": "bug",
      "image": "🐛",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F41C",
      "name": "ant",
      "image": "🐜",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F41D",
      "name": "honeybee",
      "image": "🐝",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1FAB2",
      "name": "beetle",
      "image": "🪲",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F41E",
      "name": "lady beetle",
      "image": "🐞",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F997",
      "name": "cricket",
      "image": "🦗",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1FAB3",
      "name": "cockroach",
      "image": "🪳",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F577",
      "name": "spider",
      "image": "🕷",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F578",
      "name": "spider web",
      "image": "🕸",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F982",
      "name": "scorpion",
      "image": "🦂",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F99F",
      "name": "mosquito",
      "image": "🦟",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1FAB0",
      "name": "fly",
      "image": "🪰",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1FAB1",
      "name": "worm",
      "image": "🪱",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F9A0",
      "name": "microbe",
      "image": "🦠",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F490",
      "name": "bouquet",
      "image": "💐",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F338",
      "name": "cherry blossom",
      "image": "🌸",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F4AE",
      "name": "white flower",
      "image": "💮",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1FAB7",
      "name": "lotus",
      "image": "🪷",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F3F5",
      "name": "rosette",
      "image": "🏵",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F339",
      "name": "rose",
      "image": "🌹",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F940",
      "name": "wilted flower",
      "image": "🥀",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F33A",
      "name": "hibiscus",
      "image": "🌺",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F33B",
      "name": "sunflower",
      "image": "🌻",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F33C",
      "name": "blossom",
      "image": "🌼",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F337",
      "name": "tulip",
      "image": "🌷",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F331",
      "name": "seedling",
      "image": "🌱",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1FAB4",
      "name": "potted plant",
      "image": "🪴",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F332",
      "name": "evergreen tree",
      "image": "🌲",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F333",
      "name": "deciduous tree",
      "image": "🌳",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F334",
      "name": "palm tree",
      "image": "🌴",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F335",
      "name": "cactus",
      "image": "🌵",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F33E",
      "name": "sheaf of rice",
      "image": "🌾",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F33F",
      "name": "herb",
      "image": "🌿",
      "category": "Animals & Nature"
    },
    {
      "code": "U+2618",
      "name": "shamrock",
      "image": "☘",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F340",
      "name": "four leaf clover",
      "image": "🍀",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F341",
      "name": "maple leaf",
      "image": "🍁",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F342",
      "name": "fallen leaf",
      "image": "🍂",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F343",
      "name": "leaf fluttering in wind",
      "image": "🍃",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1FAB9",
      "name": "empty nest",
      "image": "🪹",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1FABA",
      "name": "nest with eggs",
      "image": "🪺",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F344",
      "name": "mushroom",
      "image": "🍄",
      "category": "Animals & Nature"
    },
    {
      "code": "U+1F347",
      "name": "grapes",
      "image": "🍇",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F348",
      "name": "melon",
      "image": "🍈",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F349",
      "name": "watermelon",
      "image": "🍉",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F34A",
      "name": "tangerine",
      "image": "🍊",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F34B",
      "name": "lemon",
      "image": "🍋",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F34C",
      "name": "banana",
      "image": "🍌",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F34D",
      "name": "pineapple",
      "image": "🍍",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F96D",
      "name": "mango",
      "image": "🥭",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F34E",
      "name": "red apple",
      "image": "🍎",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F34F",
      "name": "green apple",
      "image": "🍏",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F350",
      "name": "pear",
      "image": "🍐",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F351",
      "name": "peach",
      "image": "🍑",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F352",
      "name": "cherries",
      "image": "🍒",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F353",
      "name": "strawberry",
      "image": "🍓",
      "category": "Food & Drink"
    },
    {
      "code": "U+1FAD0",
      "name": "blueberries",
      "image": "🫐",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F95D",
      "name": "kiwi fruit",
      "image": "🥝",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F345",
      "name": "tomato",
      "image": "🍅",
      "category": "Food & Drink"
    },
    {
      "code": "U+1FAD2",
      "name": "olive",
      "image": "🫒",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F965",
      "name": "coconut",
      "image": "🥥",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F951",
      "name": "avocado",
      "image": "🥑",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F346",
      "name": "eggplant",
      "image": "🍆",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F954",
      "name": "potato",
      "image": "🥔",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F955",
      "name": "carrot",
      "image": "🥕",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F33D",
      "name": "ear of corn",
      "image": "🌽",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F336",
      "name": "hot pepper",
      "image": "🌶",
      "category": "Food & Drink"
    },
    {
      "code": "U+1FAD1",
      "name": "bell pepper",
      "image": "🫑",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F952",
      "name": "cucumber",
      "image": "🥒",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F96C",
      "name": "leafy green",
      "image": "🥬",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F966",
      "name": "broccoli",
      "image": "🥦",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F9C4",
      "name": "garlic",
      "image": "🧄",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F9C5",
      "name": "onion",
      "image": "🧅",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F95C",
      "name": "peanuts",
      "image": "🥜",
      "category": "Food & Drink"
    },
    {
      "code": "U+1FAD8",
      "name": "beans",
      "image": "🫘",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F330",
      "name": "chestnut",
      "image": "🌰",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F35E",
      "name": "bread",
      "image": "🍞",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F950",
      "name": "croissant",
      "image": "🥐",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F956",
      "name": "baguette bread",
      "image": "🥖",
      "category": "Food & Drink"
    },
    {
      "code": "U+1FAD3",
      "name": "flatbread",
      "image": "🫓",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F968",
      "name": "pretzel",
      "image": "🥨",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F96F",
      "name": "bagel",
      "image": "🥯",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F95E",
      "name": "pancakes",
      "image": "🥞",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F9C7",
      "name": "waffle",
      "image": "🧇",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F9C0",
      "name": "cheese wedge",
      "image": "🧀",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F356",
      "name": "meat on bone",
      "image": "🍖",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F357",
      "name": "poultry leg",
      "image": "🍗",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F969",
      "name": "cut of meat",
      "image": "🥩",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F953",
      "name": "bacon",
      "image": "🥓",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F354",
      "name": "hamburger",
      "image": "🍔",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F35F",
      "name": "french fries",
      "image": "🍟",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F355",
      "name": "pizza",
      "image": "🍕",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F32D",
      "name": "hot dog",
      "image": "🌭",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F96A",
      "name": "sandwich",
      "image": "🥪",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F32E",
      "name": "taco",
      "image": "🌮",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F32F",
      "name": "burrito",
      "image": "🌯",
      "category": "Food & Drink"
    },
    {
      "code": "U+1FAD4",
      "name": "tamale",
      "image": "🫔",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F959",
      "name": "stuffed flatbread",
      "image": "🥙",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F9C6",
      "name": "falafel",
      "image": "🧆",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F95A",
      "name": "egg",
      "image": "🥚",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F373",
      "name": "cooking",
      "image": "🍳",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F958",
      "name": "shallow pan of food",
      "image": "🥘",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F372",
      "name": "pot of food",
      "image": "🍲",
      "category": "Food & Drink"
    },
    {
      "code": "U+1FAD5",
      "name": "fondue",
      "image": "🫕",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F963",
      "name": "bowl with spoon",
      "image": "🥣",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F957",
      "name": "green salad",
      "image": "🥗",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F37F",
      "name": "popcorn",
      "image": "🍿",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F9C8",
      "name": "butter",
      "image": "🧈",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F9C2",
      "name": "salt",
      "image": "🧂",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F96B",
      "name": "canned food",
      "image": "🥫",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F371",
      "name": "bento box",
      "image": "🍱",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F358",
      "name": "rice cracker",
      "image": "🍘",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F359",
      "name": "rice ball",
      "image": "🍙",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F35A",
      "name": "cooked rice",
      "image": "🍚",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F35B",
      "name": "curry rice",
      "image": "🍛",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F35C",
      "name": "steaming bowl",
      "image": "🍜",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F35D",
      "name": "spaghetti",
      "image": "🍝",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F360",
      "name": "roasted sweet potato",
      "image": "🍠",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F362",
      "name": "oden",
      "image": "🍢",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F363",
      "name": "sushi",
      "image": "🍣",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F364",
      "name": "fried shrimp",
      "image": "🍤",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F365",
      "name": "fish cake with swirl",
      "image": "🍥",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F96E",
      "name": "moon cake",
      "image": "🥮",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F361",
      "name": "dango",
      "image": "🍡",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F95F",
      "name": "dumpling",
      "image": "🥟",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F960",
      "name": "fortune cookie",
      "image": "🥠",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F961",
      "name": "takeout box",
      "image": "🥡",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F980",
      "name": "crab",
      "image": "🦀",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F99E",
      "name": "lobster",
      "image": "🦞",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F990",
      "name": "shrimp",
      "image": "🦐",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F991",
      "name": "squid",
      "image": "🦑",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F9AA",
      "name": "oyster",
      "image": "🦪",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F366",
      "name": "soft ice cream",
      "image": "🍦",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F367",
      "name": "shaved ice",
      "image": "🍧",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F368",
      "name": "ice cream",
      "image": "🍨",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F369",
      "name": "doughnut",
      "image": "🍩",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F36A",
      "name": "cookie",
      "image": "🍪",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F382",
      "name": "birthday cake",
      "image": "🎂",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F370",
      "name": "shortcake",
      "image": "🍰",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F9C1",
      "name": "cupcake",
      "image": "🧁",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F967",
      "name": "pie",
      "image": "🥧",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F36B",
      "name": "chocolate bar",
      "image": "🍫",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F36C",
      "name": "candy",
      "image": "🍬",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F36D",
      "name": "lollipop",
      "image": "🍭",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F36E",
      "name": "custard",
      "image": "🍮",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F36F",
      "name": "honey pot",
      "image": "🍯",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F37C",
      "name": "baby bottle",
      "image": "🍼",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F95B",
      "name": "glass of milk",
      "image": "🥛",
      "category": "Food & Drink"
    },
    {
      "code": "U+2615",
      "name": "hot beverage",
      "image": "☕",
      "category": "Food & Drink"
    },
    {
      "code": "U+1FAD6",
      "name": "teapot",
      "image": "🫖",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F375",
      "name": "teacup without handle",
      "image": "🍵",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F376",
      "name": "sake",
      "image": "🍶",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F37E",
      "name": "bottle with popping cork",
      "image": "🍾",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F377",
      "name": "wine glass",
      "image": "🍷",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F378",
      "name": "cocktail glass",
      "image": "🍸",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F379",
      "name": "tropical drink",
      "image": "🍹",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F37A",
      "name": "beer mug",
      "image": "🍺",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F37B",
      "name": "clinking beer mugs",
      "image": "🍻",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F942",
      "name": "clinking glasses",
      "image": "🥂",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F943",
      "name": "tumbler glass",
      "image": "🥃",
      "category": "Food & Drink"
    },
    {
      "code": "U+1FAD7",
      "name": "pouring liquid",
      "image": "🫗",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F964",
      "name": "cup with straw",
      "image": "🥤",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F9CB",
      "name": "bubble tea",
      "image": "🧋",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F9C3",
      "name": "beverage box",
      "image": "🧃",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F9C9",
      "name": "mate",
      "image": "🧉",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F9CA",
      "name": "ice",
      "image": "🧊",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F962",
      "name": "chopsticks",
      "image": "🥢",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F37D",
      "name": "fork and knife with plate",
      "image": "🍽",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F374",
      "name": "fork and knife",
      "image": "🍴",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F944",
      "name": "spoon",
      "image": "🥄",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F52A",
      "name": "kitchen knife",
      "image": "🔪",
      "category": "Food & Drink"
    },
    {
      "code": "U+1FAD9",
      "name": "jar",
      "image": "🫙",
      "category": "Food & Drink"
    },
    {
      "code": "U+1F3FA",
      "name": "amphora",
      "image": "🏺",
      "category": "Food & Drink"
    },{
      "code": "U+1F30D",
      "name": "globe showing Europe-Africa",
      "image": "🌍",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F30E",
      "name": "globe showing Americas",
      "image": "🌎",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F30F",
      "name": "globe showing Asia-Australia",
      "image": "🌏",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F310",
      "name": "globe with meridians",
      "image": "🌐",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F5FA",
      "name": "world map",
      "image": "🗺",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F5FE",
      "name": "map of Japan",
      "image": "🗾",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F9ED",
      "name": "compass",
      "image": "🧭",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3D4",
      "name": "snow-capped mountain",
      "image": "🏔",
      "category": "Travel & Places"
    },
    {
      "code": "U+26F0",
      "name": "mountain",
      "image": "⛰",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F30B",
      "name": "volcano",
      "image": "🌋",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F5FB",
      "name": "mount fuji",
      "image": "🗻",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3D5",
      "name": "camping",
      "image": "🏕",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3D6",
      "name": "beach with umbrella",
      "image": "🏖",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3DC",
      "name": "desert",
      "image": "🏜",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3DD",
      "name": "desert island",
      "image": "🏝",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3DE",
      "name": "national park",
      "image": "🏞",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3DF",
      "name": "stadium",
      "image": "🏟",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3DB",
      "name": "classical building",
      "image": "🏛",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3D7",
      "name": "building construction",
      "image": "🏗",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F9F1",
      "name": "brick",
      "image": "🧱",
      "category": "Travel & Places"
    },
    {
      "code": "U+1FAA8",
      "name": "rock",
      "image": "🪨",
      "category": "Travel & Places"
    },
    {
      "code": "U+1FAB5",
      "name": "wood",
      "image": "🪵",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6D6",
      "name": "hut",
      "image": "🛖",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3D8",
      "name": "houses",
      "image": "🏘",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3DA",
      "name": "derelict house",
      "image": "🏚",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3E0",
      "name": "house",
      "image": "🏠",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3E1",
      "name": "house with garden",
      "image": "🏡",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3E2",
      "name": "office building",
      "image": "🏢",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3E3",
      "name": "Japanese post office",
      "image": "🏣",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3E4",
      "name": "post office",
      "image": "🏤",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3E5",
      "name": "hospital",
      "image": "🏥",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3E6",
      "name": "bank",
      "image": "🏦",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3E8",
      "name": "hotel",
      "image": "🏨",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3E9",
      "name": "love hotel",
      "image": "🏩",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3EA",
      "name": "convenience store",
      "image": "🏪",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3EB",
      "name": "school",
      "image": "🏫",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3EC",
      "name": "department store",
      "image": "🏬",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3ED",
      "name": "factory",
      "image": "🏭",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3EF",
      "name": "Japanese castle",
      "image": "🏯",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3F0",
      "name": "castle",
      "image": "🏰",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F492",
      "name": "wedding",
      "image": "💒",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F5FC",
      "name": "Tokyo tower",
      "image": "🗼",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F5FD",
      "name": "Statue of Liberty",
      "image": "🗽",
      "category": "Travel & Places"
    },
    {
      "code": "U+26EA",
      "name": "church",
      "image": "⛪",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F54C",
      "name": "mosque",
      "image": "🕌",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6D5",
      "name": "hindu temple",
      "image": "🛕",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F54D",
      "name": "synagogue",
      "image": "🕍",
      "category": "Travel & Places"
    },
    {
      "code": "U+26E9",
      "name": "shinto shrine",
      "image": "⛩",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F54B",
      "name": "kaaba",
      "image": "🕋",
      "category": "Travel & Places"
    },
    {
      "code": "U+26F2",
      "name": "fountain",
      "image": "⛲",
      "category": "Travel & Places"
    },
    {
      "code": "U+26FA",
      "name": "tent",
      "image": "⛺",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F301",
      "name": "foggy",
      "image": "🌁",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F303",
      "name": "night with stars",
      "image": "🌃",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3D9",
      "name": "cityscape",
      "image": "🏙",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F304",
      "name": "sunrise over mountains",
      "image": "🌄",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F305",
      "name": "sunrise",
      "image": "🌅",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F306",
      "name": "cityscape at dusk",
      "image": "🌆",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F307",
      "name": "sunset",
      "image": "🌇",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F309",
      "name": "bridge at night",
      "image": "🌉",
      "category": "Travel & Places"
    },
    {
      "code": "U+2668",
      "name": "hot springs",
      "image": "♨",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3A0",
      "name": "carousel horse",
      "image": "🎠",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6DD",
      "name": "playground slide",
      "image": "🛝",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3A1",
      "name": "ferris wheel",
      "image": "🎡",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3A2",
      "name": "roller coaster",
      "image": "🎢",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F488",
      "name": "barber pole",
      "image": "💈",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3AA",
      "name": "circus tent",
      "image": "🎪",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F682",
      "name": "locomotive",
      "image": "🚂",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F683",
      "name": "railway car",
      "image": "🚃",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F684",
      "name": "high-speed train",
      "image": "🚄",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F685",
      "name": "bullet train",
      "image": "🚅",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F686",
      "name": "train",
      "image": "🚆",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F687",
      "name": "metro",
      "image": "🚇",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F688",
      "name": "light rail",
      "image": "🚈",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F689",
      "name": "station",
      "image": "🚉",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F68A",
      "name": "tram",
      "image": "🚊",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F69D",
      "name": "monorail",
      "image": "🚝",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F69E",
      "name": "mountain railway",
      "image": "🚞",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F68B",
      "name": "tram car",
      "image": "🚋",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F68C",
      "name": "bus",
      "image": "🚌",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F68D",
      "name": "oncoming bus",
      "image": "🚍",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F68E",
      "name": "trolleybus",
      "image": "🚎",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F690",
      "name": "minibus",
      "image": "🚐",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F691",
      "name": "ambulance",
      "image": "🚑",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F692",
      "name": "fire engine",
      "image": "🚒",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F693",
      "name": "police car",
      "image": "🚓",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F694",
      "name": "oncoming police car",
      "image": "🚔",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F695",
      "name": "taxi",
      "image": "🚕",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F696",
      "name": "oncoming taxi",
      "image": "🚖",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F697",
      "name": "automobile",
      "image": "🚗",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F698",
      "name": "oncoming automobile",
      "image": "🚘",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F699",
      "name": "sport utility vehicle",
      "image": "🚙",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6FB",
      "name": "pickup truck",
      "image": "🛻",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F69A",
      "name": "delivery truck",
      "image": "🚚",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F69B",
      "name": "articulated lorry",
      "image": "🚛",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F69C",
      "name": "tractor",
      "image": "🚜",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3CE",
      "name": "racing car",
      "image": "🏎",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F3CD",
      "name": "motorcycle",
      "image": "🏍",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6F5",
      "name": "motor scooter",
      "image": "🛵",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F9BD",
      "name": "manual wheelchair",
      "image": "🦽",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F9BC",
      "name": "motorized wheelchair",
      "image": "🦼",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6FA",
      "name": "auto rickshaw",
      "image": "🛺",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6B2",
      "name": "bicycle",
      "image": "🚲",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6F4",
      "name": "kick scooter",
      "image": "🛴",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6F9",
      "name": "skateboard",
      "image": "🛹",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6FC",
      "name": "roller skate",
      "image": "🛼",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F68F",
      "name": "bus stop",
      "image": "🚏",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6E3",
      "name": "motorway",
      "image": "🛣",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6E4",
      "name": "railway track",
      "image": "🛤",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6E2",
      "name": "oil drum",
      "image": "🛢",
      "category": "Travel & Places"
    },
    {
      "code": "U+26FD",
      "name": "fuel pump",
      "image": "⛽",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6DE",
      "name": "wheel",
      "image": "🛞",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6A8",
      "name": "police car light",
      "image": "🚨",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6A5",
      "name": "horizontal traffic light",
      "image": "🚥",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6A6",
      "name": "vertical traffic light",
      "image": "🚦",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6D1",
      "name": "stop sign",
      "image": "🛑",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6A7",
      "name": "construction",
      "image": "🚧",
      "category": "Travel & Places"
    },
    {
      "code": "U+2693",
      "name": "anchor",
      "image": "⚓",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6DF",
      "name": "ring buoy",
      "image": "🛟",
      "category": "Travel & Places"
    },
    {
      "code": "U+26F5",
      "name": "sailboat",
      "image": "⛵",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6F6",
      "name": "canoe",
      "image": "🛶",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6A4",
      "name": "speedboat",
      "image": "🚤",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6F3",
      "name": "passenger ship",
      "image": "🛳",
      "category": "Travel & Places"
    },
    {
      "code": "U+26F4",
      "name": "ferry",
      "image": "⛴",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6E5",
      "name": "motor boat",
      "image": "🛥",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6A2",
      "name": "ship",
      "image": "🚢",
      "category": "Travel & Places"
    },
    {
      "code": "U+2708",
      "name": "airplane",
      "image": "✈",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6E9",
      "name": "small airplane",
      "image": "🛩",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6EB",
      "name": "airplane departure",
      "image": "🛫",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6EC",
      "name": "airplane arrival",
      "image": "🛬",
      "category": "Travel & Places"
    },
    {
      "code": "U+1FA82",
      "name": "parachute",
      "image": "🪂",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F4BA",
      "name": "seat",
      "image": "💺",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F681",
      "name": "helicopter",
      "image": "🚁",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F69F",
      "name": "suspension railway",
      "image": "🚟",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6A0",
      "name": "mountain cableway",
      "image": "🚠",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6A1",
      "name": "aerial tramway",
      "image": "🚡",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6F0",
      "name": "satellite",
      "image": "🛰",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F680",
      "name": "rocket",
      "image": "🚀",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6F8",
      "name": "flying saucer",
      "image": "🛸",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F6CE",
      "name": "bellhop bell",
      "image": "🛎",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F9F3",
      "name": "luggage",
      "image": "🧳",
      "category": "Travel & Places"
    },
    {
      "code": "U+231B",
      "name": "hourglass done",
      "image": "⌛",
      "category": "Travel & Places"
    },
    {
      "code": "U+23F3",
      "name": "hourglass not done",
      "image": "⏳",
      "category": "Travel & Places"
    },
    {
      "code": "U+231A",
      "name": "watch",
      "image": "⌚",
      "category": "Travel & Places"
    },
    {
      "code": "U+23F0",
      "name": "alarm clock",
      "image": "⏰",
      "category": "Travel & Places"
    },
    {
      "code": "U+23F1",
      "name": "stopwatch",
      "image": "⏱",
      "category": "Travel & Places"
    },
    {
      "code": "U+23F2",
      "name": "timer clock",
      "image": "⏲",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F570",
      "name": "mantelpiece clock",
      "image": "🕰",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F55B",
      "name": "twelve o’clock",
      "image": "🕛",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F567",
      "name": "twelve-thirty",
      "image": "🕧",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F550",
      "name": "one o’clock",
      "image": "🕐",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F55C",
      "name": "one-thirty",
      "image": "🕜",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F551",
      "name": "two o’clock",
      "image": "🕑",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F55D",
      "name": "two-thirty",
      "image": "🕝",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F552",
      "name": "three o’clock",
      "image": "🕒",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F55E",
      "name": "three-thirty",
      "image": "🕞",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F553",
      "name": "four o’clock",
      "image": "🕓",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F55F",
      "name": "four-thirty",
      "image": "🕟",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F554",
      "name": "five o’clock",
      "image": "🕔",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F560",
      "name": "five-thirty",
      "image": "🕠",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F555",
      "name": "six o’clock",
      "image": "🕕",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F561",
      "name": "six-thirty",
      "image": "🕡",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F556",
      "name": "seven o’clock",
      "image": "🕖",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F562",
      "name": "seven-thirty",
      "image": "🕢",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F557",
      "name": "eight o’clock",
      "image": "🕗",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F563",
      "name": "eight-thirty",
      "image": "🕣",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F558",
      "name": "nine o’clock",
      "image": "🕘",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F564",
      "name": "nine-thirty",
      "image": "🕤",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F559",
      "name": "ten o’clock",
      "image": "🕙",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F565",
      "name": "ten-thirty",
      "image": "🕥",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F55A",
      "name": "eleven o’clock",
      "image": "🕚",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F566",
      "name": "eleven-thirty",
      "image": "🕦",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F311",
      "name": "new moon",
      "image": "🌑",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F312",
      "name": "waxing crescent moon",
      "image": "🌒",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F313",
      "name": "first quarter moon",
      "image": "🌓",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F314",
      "name": "waxing gibbous moon",
      "image": "🌔",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F315",
      "name": "full moon",
      "image": "🌕",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F316",
      "name": "waning gibbous moon",
      "image": "🌖",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F317",
      "name": "last quarter moon",
      "image": "🌗",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F318",
      "name": "waning crescent moon",
      "image": "🌘",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F319",
      "name": "crescent moon",
      "image": "🌙",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F31A",
      "name": "new moon face",
      "image": "🌚",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F31B",
      "name": "first quarter moon face",
      "image": "🌛",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F31C",
      "name": "last quarter moon face",
      "image": "🌜",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F321",
      "name": "thermometer",
      "image": "🌡",
      "category": "Travel & Places"
    },
    {
      "code": "U+2600",
      "name": "sun",
      "image": "☀",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F31D",
      "name": "full moon face",
      "image": "🌝",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F31E",
      "name": "sun with face",
      "image": "🌞",
      "category": "Travel & Places"
    },
    {
      "code": "U+1FA90",
      "name": "ringed planet",
      "image": "🪐",
      "category": "Travel & Places"
    },
    {
      "code": "U+2B50",
      "name": "star",
      "image": "⭐",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F31F",
      "name": "glowing star",
      "image": "🌟",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F320",
      "name": "shooting star",
      "image": "🌠",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F30C",
      "name": "milky way",
      "image": "🌌",
      "category": "Travel & Places"
    },
    {
      "code": "U+2601",
      "name": "cloud",
      "image": "☁",
      "category": "Travel & Places"
    },
    {
      "code": "U+26C5",
      "name": "sun behind cloud",
      "image": "⛅",
      "category": "Travel & Places"
    },
    {
      "code": "U+26C8",
      "name": "cloud with lightning and rain",
      "image": "⛈",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F324",
      "name": "sun behind small cloud",
      "image": "🌤",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F325",
      "name": "sun behind large cloud",
      "image": "🌥",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F326",
      "name": "sun behind rain cloud",
      "image": "🌦",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F327",
      "name": "cloud with rain",
      "image": "🌧",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F328",
      "name": "cloud with snow",
      "image": "🌨",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F329",
      "name": "cloud with lightning",
      "image": "🌩",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F32A",
      "name": "tornado",
      "image": "🌪",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F32B",
      "name": "fog",
      "image": "🌫",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F32C",
      "name": "wind face",
      "image": "🌬",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F300",
      "name": "cyclone",
      "image": "🌀",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F308",
      "name": "rainbow",
      "image": "🌈",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F302",
      "name": "closed umbrella",
      "image": "🌂",
      "category": "Travel & Places"
    },
    {
      "code": "U+2602",
      "name": "umbrella",
      "image": "☂",
      "category": "Travel & Places"
    },
    {
      "code": "U+2614",
      "name": "umbrella with rain drops",
      "image": "☔",
      "category": "Travel & Places"
    },
    {
      "code": "U+26F1",
      "name": "umbrella on ground",
      "image": "⛱",
      "category": "Travel & Places"
    },
    {
      "code": "U+26A1",
      "name": "high voltage",
      "image": "⚡",
      "category": "Travel & Places"
    },
    {
      "code": "U+2744",
      "name": "snowflake",
      "image": "❄",
      "category": "Travel & Places"
    },
    {
      "code": "U+2603",
      "name": "snowman",
      "image": "☃",
      "category": "Travel & Places"
    },
    {
      "code": "U+26C4",
      "name": "snowman without snow",
      "image": "⛄",
      "category": "Travel & Places"
    },
    {
      "code": "U+2604",
      "name": "comet",
      "image": "☄",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F525",
      "name": "fire",
      "image": "🔥",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F4A7",
      "name": "droplet",
      "image": "💧",
      "category": "Travel & Places"
    },
    {
      "code": "U+1F30A",
      "name": "water wave",
      "image": "🌊",
      "category": "Travel & Places"
    },  {
      "code": "U+1F383",
      "name": "jack-o-lantern",
      "image": "🎃",
      "category": "Activities"
    },
    {
      "code": "U+1F384",
      "name": "Christmas tree",
      "image": "🎄",
      "category": "Activities"
    },
    {
      "code": "U+1F386",
      "name": "fireworks",
      "image": "🎆",
      "category": "Activities"
    },
    {
      "code": "U+1F387",
      "name": "sparkler",
      "image": "🎇",
      "category": "Activities"
    },
    {
      "code": "U+1F9E8",
      "name": "firecracker",
      "image": "🧨",
      "category": "Activities"
    },
    {
      "code": "U+2728",
      "name": "sparkles",
      "image": "✨",
      "category": "Activities"
    },
    {
      "code": "U+1F388",
      "name": "balloon",
      "image": "🎈",
      "category": "Activities"
    },
    {
      "code": "U+1F389",
      "name": "party popper",
      "image": "🎉",
      "category": "Activities"
    },
    {
      "code": "U+1F38A",
      "name": "confetti ball",
      "image": "🎊",
      "category": "Activities"
    },
    {
      "code": "U+1F38B",
      "name": "tanabata tree",
      "image": "🎋",
      "category": "Activities"
    },
    {
      "code": "U+1F38D",
      "name": "pine decoration",
      "image": "🎍",
      "category": "Activities"
    },
    {
      "code": "U+1F38E",
      "name": "Japanese dolls",
      "image": "🎎",
      "category": "Activities"
    },
    {
      "code": "U+1F38F",
      "name": "carp streamer",
      "image": "🎏",
      "category": "Activities"
    },
    {
      "code": "U+1F390",
      "name": "wind chime",
      "image": "🎐",
      "category": "Activities"
    },
    {
      "code": "U+1F391",
      "name": "moon viewing ceremony",
      "image": "🎑",
      "category": "Activities"
    },
    {
      "code": "U+1F9E7",
      "name": "red envelope",
      "image": "🧧",
      "category": "Activities"
    },
    {
      "code": "U+1F380",
      "name": "ribbon",
      "image": "🎀",
      "category": "Activities"
    },
    {
      "code": "U+1F381",
      "name": "wrapped gift",
      "image": "🎁",
      "category": "Activities"
    },
    {
      "code": "U+1F397",
      "name": "reminder ribbon",
      "image": "🎗",
      "category": "Activities"
    },
    {
      "code": "U+1F39F",
      "name": "admission tickets",
      "image": "🎟",
      "category": "Activities"
    },
    {
      "code": "U+1F3AB",
      "name": "ticket",
      "image": "🎫",
      "category": "Activities"
    },
    {
      "code": "U+1F396",
      "name": "military medal",
      "image": "🎖",
      "category": "Activities"
    },
    {
      "code": "U+1F3C6",
      "name": "trophy",
      "image": "🏆",
      "category": "Activities"
    },
    {
      "code": "U+1F3C5",
      "name": "sports medal",
      "image": "🏅",
      "category": "Activities"
    },
    {
      "code": "U+1F947",
      "name": "1st place medal",
      "image": "🥇",
      "category": "Activities"
    },
    {
      "code": "U+1F948",
      "name": "2nd place medal",
      "image": "🥈",
      "category": "Activities"
    },
    {
      "code": "U+1F949",
      "name": "3rd place medal",
      "image": "🥉",
      "category": "Activities"
    },
    {
      "code": "U+26BD",
      "name": "soccer ball",
      "image": "⚽",
      "category": "Activities"
    },
    {
      "code": "U+26BE",
      "name": "baseball",
      "image": "⚾",
      "category": "Activities"
    },
    {
      "code": "U+1F94E",
      "name": "softball",
      "image": "🥎",
      "category": "Activities"
    },
    {
      "code": "U+1F3C0",
      "name": "basketball",
      "image": "🏀",
      "category": "Activities"
    },
    {
      "code": "U+1F3D0",
      "name": "volleyball",
      "image": "🏐",
      "category": "Activities"
    },
    {
      "code": "U+1F3C8",
      "name": "american football",
      "image": "🏈",
      "category": "Activities"
    },
    {
      "code": "U+1F3C9",
      "name": "rugby football",
      "image": "🏉",
      "category": "Activities"
    },
    {
      "code": "U+1F3BE",
      "name": "tennis",
      "image": "🎾",
      "category": "Activities"
    },
    {
      "code": "U+1F94F",
      "name": "flying disc",
      "image": "🥏",
      "category": "Activities"
    },
    {
      "code": "U+1F3B3",
      "name": "bowling",
      "image": "🎳",
      "category": "Activities"
    },
    {
      "code": "U+1F3CF",
      "name": "cricket game",
      "image": "🏏",
      "category": "Activities"
    },
    {
      "code": "U+1F3D1",
      "name": "field hockey",
      "image": "🏑",
      "category": "Activities"
    },
    {
      "code": "U+1F3D2",
      "name": "ice hockey",
      "image": "🏒",
      "category": "Activities"
    },
    {
      "code": "U+1F94D",
      "name": "lacrosse",
      "image": "🥍",
      "category": "Activities"
    },
    {
      "code": "U+1F3D3",
      "name": "ping pong",
      "image": "🏓",
      "category": "Activities"
    },
    {
      "code": "U+1F3F8",
      "name": "badminton",
      "image": "🏸",
      "category": "Activities"
    },
    {
      "code": "U+1F94A",
      "name": "boxing glove",
      "image": "🥊",
      "category": "Activities"
    },
    {
      "code": "U+1F94B",
      "name": "martial arts uniform",
      "image": "🥋",
      "category": "Activities"
    },
    {
      "code": "U+1F945",
      "name": "goal net",
      "image": "🥅",
      "category": "Activities"
    },
    {
      "code": "U+26F3",
      "name": "flag in hole",
      "image": "⛳",
      "category": "Activities"
    },
    {
      "code": "U+26F8",
      "name": "ice skate",
      "image": "⛸",
      "category": "Activities"
    },
    {
      "code": "U+1F3A3",
      "name": "fishing pole",
      "image": "🎣",
      "category": "Activities"
    },
    {
      "code": "U+1F93F",
      "name": "diving mask",
      "image": "🤿",
      "category": "Activities"
    },
    {
      "code": "U+1F3BD",
      "name": "running shirt",
      "image": "🎽",
      "category": "Activities"
    },
    {
      "code": "U+1F3BF",
      "name": "skis",
      "image": "🎿",
      "category": "Activities"
    },
    {
      "code": "U+1F6F7",
      "name": "sled",
      "image": "🛷",
      "category": "Activities"
    },
    {
      "code": "U+1F94C",
      "name": "curling stone",
      "image": "🥌",
      "category": "Activities"
    },
    {
      "code": "U+1F3AF",
      "name": "bullseye",
      "image": "🎯",
      "category": "Activities"
    },
    {
      "code": "U+1FA80",
      "name": "yo-yo",
      "image": "🪀",
      "category": "Activities"
    },
    {
      "code": "U+1FA81",
      "name": "kite",
      "image": "🪁",
      "category": "Activities"
    },
    {
      "code": "U+1F52B",
      "name": "water pistol",
      "image": "🔫",
      "category": "Activities"
    },
    {
      "code": "U+1F3B1",
      "name": "pool 8 ball",
      "image": "🎱",
      "category": "Activities"
    },
    {
      "code": "U+1F52E",
      "name": "crystal ball",
      "image": "🔮",
      "category": "Activities"
    },
    {
      "code": "U+1FA84",
      "name": "magic wand",
      "image": "🪄",
      "category": "Activities"
    },
    {
      "code": "U+1F3AE",
      "name": "video game",
      "image": "🎮",
      "category": "Activities"
    },
    {
      "code": "U+1F579",
      "name": "joystick",
      "image": "🕹",
      "category": "Activities"
    },
    {
      "code": "U+1F3B0",
      "name": "slot machine",
      "image": "🎰",
      "category": "Activities"
    },
    {
      "code": "U+1F3B2",
      "name": "game die",
      "image": "🎲",
      "category": "Activities"
    },
    {
      "code": "U+1F9E9",
      "name": "puzzle piece",
      "image": "🧩",
      "category": "Activities"
    },
    {
      "code": "U+1F9F8",
      "name": "teddy bear",
      "image": "🧸",
      "category": "Activities"
    },
    {
      "code": "U+1FA85",
      "name": "piñata",
      "image": "🪅",
      "category": "Activities"
    },
    {
      "code": "U+1FAA9",
      "name": "mirror ball",
      "image": "🪩",
      "category": "Activities"
    },
    {
      "code": "U+1FA86",
      "name": "nesting dolls",
      "image": "🪆",
      "category": "Activities"
    },
    {
      "code": "U+2660",
      "name": "spade suit",
      "image": "♠",
      "category": "Activities"
    },
    {
      "code": "U+2665",
      "name": "heart suit",
      "image": "♥",
      "category": "Activities"
    },
    {
      "code": "U+2666",
      "name": "diamond suit",
      "image": "♦",
      "category": "Activities"
    },
    {
      "code": "U+2663",
      "name": "club suit",
      "image": "♣",
      "category": "Activities"
    },
    {
      "code": "U+265F",
      "name": "chess pawn",
      "image": "♟",
      "category": "Activities"
    },
    {
      "code": "U+1F0CF",
      "name": "joker",
      "image": "🃏",
      "category": "Activities"
    },
    {
      "code": "U+1F004",
      "name": "mahjong red dragon",
      "image": "🀄",
      "category": "Activities"
    },
    {
      "code": "U+1F3B4",
      "name": "flower playing cards",
      "image": "🎴",
      "category": "Activities"
    },
    {
      "code": "U+1F3AD",
      "name": "performing arts",
      "image": "🎭",
      "category": "Activities"
    },
    {
      "code": "U+1F5BC",
      "name": "framed picture",
      "image": "🖼",
      "category": "Activities"
    },
    {
      "code": "U+1F3A8",
      "name": "artist palette",
      "image": "🎨",
      "category": "Activities"
    },
    {
      "code": "U+1F9F5",
      "name": "thread",
      "image": "🧵",
      "category": "Activities"
    },
    {
      "code": "U+1FAA1",
      "name": "sewing needle",
      "image": "🪡",
      "category": "Activities"
    },
    {
      "code": "U+1F9F6",
      "name": "yarn",
      "image": "🧶",
      "category": "Activities"
    },
    {
      "code": "U+1FAA2",
      "name": "knot",
      "image": "🪢",
      "category": "Activities"
    },  {
      "code": "U+1F453",
      "name": "glasses",
      "image": "👓",
      "category": "Objects"
    },
    {
      "code": "U+1F576",
      "name": "sunglasses",
      "image": "🕶",
      "category": "Objects"
    },
    {
      "code": "U+1F97D",
      "name": "goggles",
      "image": "🥽",
      "category": "Objects"
    },
    {
      "code": "U+1F97C",
      "name": "lab coat",
      "image": "🥼",
      "category": "Objects"
    },
    {
      "code": "U+1F9BA",
      "name": "safety vest",
      "image": "🦺",
      "category": "Objects"
    },
    {
      "code": "U+1F454",
      "name": "necktie",
      "image": "👔",
      "category": "Objects"
    },
    {
      "code": "U+1F455",
      "name": "t-shirt",
      "image": "👕",
      "category": "Objects"
    },
    {
      "code": "U+1F456",
      "name": "jeans",
      "image": "👖",
      "category": "Objects"
    },
    {
      "code": "U+1F9E3",
      "name": "scarf",
      "image": "🧣",
      "category": "Objects"
    },
    {
      "code": "U+1F9E4",
      "name": "gloves",
      "image": "🧤",
      "category": "Objects"
    },
    {
      "code": "U+1F9E5",
      "name": "coat",
      "image": "🧥",
      "category": "Objects"
    },
    {
      "code": "U+1F9E6",
      "name": "socks",
      "image": "🧦",
      "category": "Objects"
    },
    {
      "code": "U+1F457",
      "name": "dress",
      "image": "👗",
      "category": "Objects"
    },
    {
      "code": "U+1F458",
      "name": "kimono",
      "image": "👘",
      "category": "Objects"
    },
    {
      "code": "U+1F97B",
      "name": "sari",
      "image": "🥻",
      "category": "Objects"
    },
    {
      "code": "U+1FA71",
      "name": "one-piece swimsuit",
      "image": "🩱",
      "category": "Objects"
    },
    {
      "code": "U+1FA72",
      "name": "briefs",
      "image": "🩲",
      "category": "Objects"
    },
    {
      "code": "U+1FA73",
      "name": "shorts",
      "image": "🩳",
      "category": "Objects"
    },
    {
      "code": "U+1F459",
      "name": "bikini",
      "image": "👙",
      "category": "Objects"
    },
    {
      "code": "U+1F45A",
      "name": "woman’s clothes",
      "image": "👚",
      "category": "Objects"
    },
    {
      "code": "U+1F45B",
      "name": "purse",
      "image": "👛",
      "category": "Objects"
    },
    {
      "code": "U+1F45C",
      "name": "handbag",
      "image": "👜",
      "category": "Objects"
    },
    {
      "code": "U+1F45D",
      "name": "clutch bag",
      "image": "👝",
      "category": "Objects"
    },
    {
      "code": "U+1F6CD",
      "name": "shopping bags",
      "image": "🛍",
      "category": "Objects"
    },
    {
      "code": "U+1F392",
      "name": "backpack",
      "image": "🎒",
      "category": "Objects"
    },
    {
      "code": "U+1FA74",
      "name": "thong sandal",
      "image": "🩴",
      "category": "Objects"
    },
    {
      "code": "U+1F45E",
      "name": "man’s shoe",
      "image": "👞",
      "category": "Objects"
    },
    {
      "code": "U+1F45F",
      "name": "running shoe",
      "image": "👟",
      "category": "Objects"
    },
    {
      "code": "U+1F97E",
      "name": "hiking boot",
      "image": "🥾",
      "category": "Objects"
    },
    {
      "code": "U+1F97F",
      "name": "flat shoe",
      "image": "🥿",
      "category": "Objects"
    },
    {
      "code": "U+1F460",
      "name": "high-heeled shoe",
      "image": "👠",
      "category": "Objects"
    },
    {
      "code": "U+1F461",
      "name": "woman’s sandal",
      "image": "👡",
      "category": "Objects"
    },
    {
      "code": "U+1FA70",
      "name": "ballet shoes",
      "image": "🩰",
      "category": "Objects"
    },
    {
      "code": "U+1F462",
      "name": "woman’s boot",
      "image": "👢",
      "category": "Objects"
    },
    {
      "code": "U+1F451",
      "name": "crown",
      "image": "👑",
      "category": "Objects"
    },
    {
      "code": "U+1F452",
      "name": "woman’s hat",
      "image": "👒",
      "category": "Objects"
    },
    {
      "code": "U+1F3A9",
      "name": "top hat",
      "image": "🎩",
      "category": "Objects"
    },
    {
      "code": "U+1F393",
      "name": "graduation cap",
      "image": "🎓",
      "category": "Objects"
    },
    {
      "code": "U+1F9E2",
      "name": "billed cap",
      "image": "🧢",
      "category": "Objects"
    },
    {
      "code": "U+1FA96",
      "name": "military helmet",
      "image": "🪖",
      "category": "Objects"
    },
    {
      "code": "U+26D1",
      "name": "rescue worker’s helmet",
      "image": "⛑",
      "category": "Objects"
    },
    {
      "code": "U+1F4FF",
      "name": "prayer beads",
      "image": "📿",
      "category": "Objects"
    },
    {
      "code": "U+1F484",
      "name": "lipstick",
      "image": "💄",
      "category": "Objects"
    },
    {
      "code": "U+1F48D",
      "name": "ring",
      "image": "💍",
      "category": "Objects"
    },
    {
      "code": "U+1F48E",
      "name": "gem stone",
      "image": "💎",
      "category": "Objects"
    },
    {
      "code": "U+1F507",
      "name": "muted speaker",
      "image": "🔇",
      "category": "Objects"
    },
    {
      "code": "U+1F508",
      "name": "speaker low volume",
      "image": "🔈",
      "category": "Objects"
    },
    {
      "code": "U+1F509",
      "name": "speaker medium volume",
      "image": "🔉",
      "category": "Objects"
    },
    {
      "code": "U+1F50A",
      "name": "speaker high volume",
      "image": "🔊",
      "category": "Objects"
    },
    {
      "code": "U+1F4E2",
      "name": "loudspeaker",
      "image": "📢",
      "category": "Objects"
    },
    {
      "code": "U+1F4E3",
      "name": "megaphone",
      "image": "📣",
      "category": "Objects"
    },
    {
      "code": "U+1F4EF",
      "name": "postal horn",
      "image": "📯",
      "category": "Objects"
    },
    {
      "code": "U+1F514",
      "name": "bell",
      "image": "🔔",
      "category": "Objects"
    },
    {
      "code": "U+1F515",
      "name": "bell with slash",
      "image": "🔕",
      "category": "Objects"
    },
    {
      "code": "U+1F3BC",
      "name": "musical score",
      "image": "🎼",
      "category": "Objects"
    },
    {
      "code": "U+1F3B5",
      "name": "musical note",
      "image": "🎵",
      "category": "Objects"
    },
    {
      "code": "U+1F3B6",
      "name": "musical notes",
      "image": "🎶",
      "category": "Objects"
    },
    {
      "code": "U+1F399",
      "name": "studio microphone",
      "image": "🎙",
      "category": "Objects"
    },
    {
      "code": "U+1F39A",
      "name": "level slider",
      "image": "🎚",
      "category": "Objects"
    },
    {
      "code": "U+1F39B",
      "name": "control knobs",
      "image": "🎛",
      "category": "Objects"
    },
    {
      "code": "U+1F3A4",
      "name": "microphone",
      "image": "🎤",
      "category": "Objects"
    },
    {
      "code": "U+1F3A7",
      "name": "headphone",
      "image": "🎧",
      "category": "Objects"
    },
    {
      "code": "U+1F4FB",
      "name": "radio",
      "image": "📻",
      "category": "Objects"
    },
    {
      "code": "U+1F3B7",
      "name": "saxophone",
      "image": "🎷",
      "category": "Objects"
    },
    {
      "code": "U+1FA97",
      "name": "accordion",
      "image": "🪗",
      "category": "Objects"
    },
    {
      "code": "U+1F3B8",
      "name": "guitar",
      "image": "🎸",
      "category": "Objects"
    },
    {
      "code": "U+1F3B9",
      "name": "musical keyboard",
      "image": "🎹",
      "category": "Objects"
    },
    {
      "code": "U+1F3BA",
      "name": "trumpet",
      "image": "🎺",
      "category": "Objects"
    },
    {
      "code": "U+1F3BB",
      "name": "violin",
      "image": "🎻",
      "category": "Objects"
    },
    {
      "code": "U+1FA95",
      "name": "banjo",
      "image": "🪕",
      "category": "Objects"
    },
    {
      "code": "U+1F941",
      "name": "drum",
      "image": "🥁",
      "category": "Objects"
    },
    {
      "code": "U+1FA98",
      "name": "long drum",
      "image": "🪘",
      "category": "Objects"
    },
    {
      "code": "U+1F4F1",
      "name": "mobile phone",
      "image": "📱",
      "category": "Objects"
    },
    {
      "code": "U+1F4F2",
      "name": "mobile phone with arrow",
      "image": "📲",
      "category": "Objects"
    },
    {
      "code": "U+260E",
      "name": "telephone",
      "image": "☎",
      "category": "Objects"
    },
    {
      "code": "U+1F4DE",
      "name": "telephone receiver",
      "image": "📞",
      "category": "Objects"
    },
    {
      "code": "U+1F4DF",
      "name": "pager",
      "image": "📟",
      "category": "Objects"
    },
    {
      "code": "U+1F4E0",
      "name": "fax machine",
      "image": "📠",
      "category": "Objects"
    },
    {
      "code": "U+1F50B",
      "name": "battery",
      "image": "🔋",
      "category": "Objects"
    },
    {
      "code": "U+1FAAB",
      "name": "low battery",
      "image": "🪫",
      "category": "Objects"
    },
    {
      "code": "U+1F50C",
      "name": "electric plug",
      "image": "🔌",
      "category": "Objects"
    },
    {
      "code": "U+1F4BB",
      "name": "laptop",
      "image": "💻",
      "category": "Objects"
    },
    {
      "code": "U+1F5A5",
      "name": "desktop computer",
      "image": "🖥",
      "category": "Objects"
    },
    {
      "code": "U+1F5A8",
      "name": "printer",
      "image": "🖨",
      "category": "Objects"
    },
    {
      "code": "U+2328",
      "name": "keyboard",
      "image": "⌨",
      "category": "Objects"
    },
    {
      "code": "U+1F5B1",
      "name": "computer mouse",
      "image": "🖱",
      "category": "Objects"
    },
    {
      "code": "U+1F5B2",
      "name": "trackball",
      "image": "🖲",
      "category": "Objects"
    },
    {
      "code": "U+1F4BD",
      "name": "computer disk",
      "image": "💽",
      "category": "Objects"
    },
    {
      "code": "U+1F4BE",
      "name": "floppy disk",
      "image": "💾",
      "category": "Objects"
    },
    {
      "code": "U+1F4BF",
      "name": "optical disk",
      "image": "💿",
      "category": "Objects"
    },
    {
      "code": "U+1F4C0",
      "name": "dvd",
      "image": "📀",
      "category": "Objects"
    },
    {
      "code": "U+1F9EE",
      "name": "abacus",
      "image": "🧮",
      "category": "Objects"
    },
    {
      "code": "U+1F3A5",
      "name": "movie camera",
      "image": "🎥",
      "category": "Objects"
    },
    {
      "code": "U+1F39E",
      "name": "film frames",
      "image": "🎞",
      "category": "Objects"
    },
    {
      "code": "U+1F4FD",
      "name": "film projector",
      "image": "📽",
      "category": "Objects"
    },
    {
      "code": "U+1F3AC",
      "name": "clapper board",
      "image": "🎬",
      "category": "Objects"
    },
    {
      "code": "U+1F4FA",
      "name": "television",
      "image": "📺",
      "category": "Objects"
    },
    {
      "code": "U+1F4F7",
      "name": "camera",
      "image": "📷",
      "category": "Objects"
    },
    {
      "code": "U+1F4F8",
      "name": "camera with flash",
      "image": "📸",
      "category": "Objects"
    },
    {
      "code": "U+1F4F9",
      "name": "video camera",
      "image": "📹",
      "category": "Objects"
    },
    {
      "code": "U+1F4FC",
      "name": "videocassette",
      "image": "📼",
      "category": "Objects"
    },
    {
      "code": "U+1F50D",
      "name": "magnifying glass tilted left",
      "image": "🔍",
      "category": "Objects"
    },
    {
      "code": "U+1F50E",
      "name": "magnifying glass tilted right",
      "image": "🔎",
      "category": "Objects"
    },
    {
      "code": "U+1F56F",
      "name": "candle",
      "image": "🕯",
      "category": "Objects"
    },
    {
      "code": "U+1F4A1",
      "name": "light bulb",
      "image": "💡",
      "category": "Objects"
    },
    {
      "code": "U+1F526",
      "name": "flashlight",
      "image": "🔦",
      "category": "Objects"
    },
    {
      "code": "U+1F3EE",
      "name": "red paper lantern",
      "image": "🏮",
      "category": "Objects"
    },
    {
      "code": "U+1FA94",
      "name": "diya lamp",
      "image": "🪔",
      "category": "Objects"
    },
    {
      "code": "U+1F4D4",
      "name": "notebook with decorative cover",
      "image": "📔",
      "category": "Objects"
    },
    {
      "code": "U+1F4D5",
      "name": "closed book",
      "image": "📕",
      "category": "Objects"
    },
    {
      "code": "U+1F4D6",
      "name": "open book",
      "image": "📖",
      "category": "Objects"
    },
    {
      "code": "U+1F4D7",
      "name": "green book",
      "image": "📗",
      "category": "Objects"
    },
    {
      "code": "U+1F4D8",
      "name": "blue book",
      "image": "📘",
      "category": "Objects"
    },
    {
      "code": "U+1F4D9",
      "name": "orange book",
      "image": "📙",
      "category": "Objects"
    },
    {
      "code": "U+1F4DA",
      "name": "books",
      "image": "📚",
      "category": "Objects"
    },
    {
      "code": "U+1F4D3",
      "name": "notebook",
      "image": "📓",
      "category": "Objects"
    },
    {
      "code": "U+1F4D2",
      "name": "ledger",
      "image": "📒",
      "category": "Objects"
    },
    {
      "code": "U+1F4C3",
      "name": "page with curl",
      "image": "📃",
      "category": "Objects"
    },
    {
      "code": "U+1F4DC",
      "name": "scroll",
      "image": "📜",
      "category": "Objects"
    },
    {
      "code": "U+1F4C4",
      "name": "page facing up",
      "image": "📄",
      "category": "Objects"
    },
    {
      "code": "U+1F4F0",
      "name": "newspaper",
      "image": "📰",
      "category": "Objects"
    },
    {
      "code": "U+1F5DE",
      "name": "rolled-up newspaper",
      "image": "🗞",
      "category": "Objects"
    },
    {
      "code": "U+1F4D1",
      "name": "bookmark tabs",
      "image": "📑",
      "category": "Objects"
    },
    {
      "code": "U+1F516",
      "name": "bookmark",
      "image": "🔖",
      "category": "Objects"
    },
    {
      "code": "U+1F3F7",
      "name": "label",
      "image": "🏷",
      "category": "Objects"
    },
    {
      "code": "U+1F4B0",
      "name": "money bag",
      "image": "💰",
      "category": "Objects"
    },
    {
      "code": "U+1FA99",
      "name": "coin",
      "image": "🪙",
      "category": "Objects"
    },
    {
      "code": "U+1F4B4",
      "name": "yen banknote",
      "image": "💴",
      "category": "Objects"
    },
    {
      "code": "U+1F4B5",
      "name": "dollar banknote",
      "image": "💵",
      "category": "Objects"
    },
    {
      "code": "U+1F4B6",
      "name": "euro banknote",
      "image": "💶",
      "category": "Objects"
    },
    {
      "code": "U+1F4B7",
      "name": "pound banknote",
      "image": "💷",
      "category": "Objects"
    },
    {
      "code": "U+1F4B8",
      "name": "money with wings",
      "image": "💸",
      "category": "Objects"
    },
    {
      "code": "U+1F4B3",
      "name": "credit card",
      "image": "💳",
      "category": "Objects"
    },
    {
      "code": "U+1F9FE",
      "name": "receipt",
      "image": "🧾",
      "category": "Objects"
    },
    {
      "code": "U+1F4B9",
      "name": "chart increasing with yen",
      "image": "💹",
      "category": "Objects"
    },
    {
      "code": "U+2709",
      "name": "envelope",
      "image": "✉",
      "category": "Objects"
    },
    {
      "code": "U+1F4E7",
      "name": "e-mail",
      "image": "📧",
      "category": "Objects"
    },
    {
      "code": "U+1F4E8",
      "name": "incoming envelope",
      "image": "📨",
      "category": "Objects"
    },
    {
      "code": "U+1F4E9",
      "name": "envelope with arrow",
      "image": "📩",
      "category": "Objects"
    },
    {
      "code": "U+1F4E4",
      "name": "outbox tray",
      "image": "📤",
      "category": "Objects"
    },
    {
      "code": "U+1F4E5",
      "name": "inbox tray",
      "image": "📥",
      "category": "Objects"
    },
    {
      "code": "U+1F4E6",
      "name": "package",
      "image": "📦",
      "category": "Objects"
    },
    {
      "code": "U+1F4EB",
      "name": "closed mailbox with raised flag",
      "image": "📫",
      "category": "Objects"
    },
    {
      "code": "U+1F4EA",
      "name": "closed mailbox with lowered flag",
      "image": "📪",
      "category": "Objects"
    },
    {
      "code": "U+1F4EC",
      "name": "open mailbox with raised flag",
      "image": "📬",
      "category": "Objects"
    },
    {
      "code": "U+1F4ED",
      "name": "open mailbox with lowered flag",
      "image": "📭",
      "category": "Objects"
    },
    {
      "code": "U+1F4EE",
      "name": "postbox",
      "image": "📮",
      "category": "Objects"
    },
    {
      "code": "U+1F5F3",
      "name": "ballot box with ballot",
      "image": "🗳",
      "category": "Objects"
    },
    {
      "code": "U+270F",
      "name": "pencil",
      "image": "✏",
      "category": "Objects"
    },
    {
      "code": "U+2712",
      "name": "black nib",
      "image": "✒",
      "category": "Objects"
    },
    {
      "code": "U+1F58B",
      "name": "fountain pen",
      "image": "🖋",
      "category": "Objects"
    },
    {
      "code": "U+1F58A",
      "name": "pen",
      "image": "🖊",
      "category": "Objects"
    },
    {
      "code": "U+1F58C",
      "name": "paintbrush",
      "image": "🖌",
      "category": "Objects"
    },
    {
      "code": "U+1F58D",
      "name": "crayon",
      "image": "🖍",
      "category": "Objects"
    },
    {
      "code": "U+1F4DD",
      "name": "memo",
      "image": "📝",
      "category": "Objects"
    },
    {
      "code": "U+1F4BC",
      "name": "briefcase",
      "image": "💼",
      "category": "Objects"
    },
    {
      "code": "U+1F4C1",
      "name": "file folder",
      "image": "📁",
      "category": "Objects"
    },
    {
      "code": "U+1F4C2",
      "name": "open file folder",
      "image": "📂",
      "category": "Objects"
    },
    {
      "code": "U+1F5C2",
      "name": "card index dividers",
      "image": "🗂",
      "category": "Objects"
    },
    {
      "code": "U+1F4C5",
      "name": "calendar",
      "image": "📅",
      "category": "Objects"
    },
    {
      "code": "U+1F4C6",
      "name": "tear-off calendar",
      "image": "📆",
      "category": "Objects"
    },
    {
      "code": "U+1F5D2",
      "name": "spiral notepad",
      "image": "🗒",
      "category": "Objects"
    },
    {
      "code": "U+1F5D3",
      "name": "spiral calendar",
      "image": "🗓",
      "category": "Objects"
    },
    {
      "code": "U+1F4C7",
      "name": "card index",
      "image": "📇",
      "category": "Objects"
    },
    {
      "code": "U+1F4C8",
      "name": "chart increasing",
      "image": "📈",
      "category": "Objects"
    },
    {
      "code": "U+1F4C9",
      "name": "chart decreasing",
      "image": "📉",
      "category": "Objects"
    },
    {
      "code": "U+1F4CA",
      "name": "bar chart",
      "image": "📊",
      "category": "Objects"
    },
    {
      "code": "U+1F4CB",
      "name": "clipboard",
      "image": "📋",
      "category": "Objects"
    },
    {
      "code": "U+1F4CC",
      "name": "pushpin",
      "image": "📌",
      "category": "Objects"
    },
    {
      "code": "U+1F4CD",
      "name": "round pushpin",
      "image": "📍",
      "category": "Objects"
    },
    {
      "code": "U+1F4CE",
      "name": "paperclip",
      "image": "📎",
      "category": "Objects"
    },
    {
      "code": "U+1F587",
      "name": "linked paperclips",
      "image": "🖇",
      "category": "Objects"
    },
    {
      "code": "U+1F4CF",
      "name": "straight ruler",
      "image": "📏",
      "category": "Objects"
    },
    {
      "code": "U+1F4D0",
      "name": "triangular ruler",
      "image": "📐",
      "category": "Objects"
    },
    {
      "code": "U+2702",
      "name": "scissors",
      "image": "✂",
      "category": "Objects"
    },
    {
      "code": "U+1F5C3",
      "name": "card file box",
      "image": "🗃",
      "category": "Objects"
    },
    {
      "code": "U+1F5C4",
      "name": "file cabinet",
      "image": "🗄",
      "category": "Objects"
    },
    {
      "code": "U+1F5D1",
      "name": "wastebasket",
      "image": "🗑",
      "category": "Objects"
    },
    {
      "code": "U+1F512",
      "name": "locked",
      "image": "🔒",
      "category": "Objects"
    },
    {
      "code": "U+1F513",
      "name": "unlocked",
      "image": "🔓",
      "category": "Objects"
    },
    {
      "code": "U+1F50F",
      "name": "locked with pen",
      "image": "🔏",
      "category": "Objects"
    },
    {
      "code": "U+1F510",
      "name": "locked with key",
      "image": "🔐",
      "category": "Objects"
    },
    {
      "code": "U+1F511",
      "name": "key",
      "image": "🔑",
      "category": "Objects"
    },
    {
      "code": "U+1F5DD",
      "name": "old key",
      "image": "🗝",
      "category": "Objects"
    },
    {
      "code": "U+1F528",
      "name": "hammer",
      "image": "🔨",
      "category": "Objects"
    },
    {
      "code": "U+1FA93",
      "name": "axe",
      "image": "🪓",
      "category": "Objects"
    },
    {
      "code": "U+26CF",
      "name": "pick",
      "image": "⛏",
      "category": "Objects"
    },
    {
      "code": "U+2692",
      "name": "hammer and pick",
      "image": "⚒",
      "category": "Objects"
    },
    {
      "code": "U+1F6E0",
      "name": "hammer and wrench",
      "image": "🛠",
      "category": "Objects"
    },
    {
      "code": "U+1F5E1",
      "name": "dagger",
      "image": "🗡",
      "category": "Objects"
    },
    {
      "code": "U+2694",
      "name": "crossed swords",
      "image": "⚔",
      "category": "Objects"
    },
    {
      "code": "U+1F4A3",
      "name": "bomb",
      "image": "💣",
      "category": "Objects"
    },
    {
      "code": "U+1FA83",
      "name": "boomerang",
      "image": "🪃",
      "category": "Objects"
    },
    {
      "code": "U+1F3F9",
      "name": "bow and arrow",
      "image": "🏹",
      "category": "Objects"
    },
    {
      "code": "U+1F6E1",
      "name": "shield",
      "image": "🛡",
      "category": "Objects"
    },
    {
      "code": "U+1FA9A",
      "name": "carpentry saw",
      "image": "🪚",
      "category": "Objects"
    },
    {
      "code": "U+1F527",
      "name": "wrench",
      "image": "🔧",
      "category": "Objects"
    },
    {
      "code": "U+1FA9B",
      "name": "screwdriver",
      "image": "🪛",
      "category": "Objects"
    },
    {
      "code": "U+1F529",
      "name": "nut and bolt",
      "image": "🔩",
      "category": "Objects"
    },
    {
      "code": "U+2699",
      "name": "gear",
      "image": "⚙",
      "category": "Objects"
    },
    {
      "code": "U+1F5DC",
      "name": "clamp",
      "image": "🗜",
      "category": "Objects"
    },
    {
      "code": "U+2696",
      "name": "balance scale",
      "image": "⚖",
      "category": "Objects"
    },
    {
      "code": "U+1F9AF",
      "name": "white cane",
      "image": "🦯",
      "category": "Objects"
    },
    {
      "code": "U+1F517",
      "name": "link",
      "image": "🔗",
      "category": "Objects"
    },
    {
      "code": "U+26D3",
      "name": "chains",
      "image": "⛓",
      "category": "Objects"
    },
    {
      "code": "U+1FA9D",
      "name": "hook",
      "image": "🪝",
      "category": "Objects"
    },
    {
      "code": "U+1F9F0",
      "name": "toolbox",
      "image": "🧰",
      "category": "Objects"
    },
    {
      "code": "U+1F9F2",
      "name": "magnet",
      "image": "🧲",
      "category": "Objects"
    },
    {
      "code": "U+1FA9C",
      "name": "ladder",
      "image": "🪜",
      "category": "Objects"
    },
    {
      "code": "U+2697",
      "name": "alembic",
      "image": "⚗",
      "category": "Objects"
    },
    {
      "code": "U+1F9EA",
      "name": "test tube",
      "image": "🧪",
      "category": "Objects"
    },
    {
      "code": "U+1F9EB",
      "name": "petri dish",
      "image": "🧫",
      "category": "Objects"
    },
    {
      "code": "U+1F9EC",
      "name": "dna",
      "image": "🧬",
      "category": "Objects"
    },
    {
      "code": "U+1F52C",
      "name": "microscope",
      "image": "🔬",
      "category": "Objects"
    },
    {
      "code": "U+1F52D",
      "name": "telescope",
      "image": "🔭",
      "category": "Objects"
    },
    {
      "code": "U+1F4E1",
      "name": "satellite antenna",
      "image": "📡",
      "category": "Objects"
    },
    {
      "code": "U+1F489",
      "name": "syringe",
      "image": "💉",
      "category": "Objects"
    },
    {
      "code": "U+1FA78",
      "name": "drop of blood",
      "image": "🩸",
      "category": "Objects"
    },
    {
      "code": "U+1F48A",
      "name": "pill",
      "image": "💊",
      "category": "Objects"
    },
    {
      "code": "U+1FA79",
      "name": "adhesive bandage",
      "image": "🩹",
      "category": "Objects"
    },
    {
      "code": "U+1FA7C",
      "name": "crutch",
      "image": "🩼",
      "category": "Objects"
    },
    {
      "code": "U+1FA7A",
      "name": "stethoscope",
      "image": "🩺",
      "category": "Objects"
    },
    {
      "code": "U+1FA7B",
      "name": "x-ray",
      "image": "🩻",
      "category": "Objects"
    },
    {
      "code": "U+1F6AA",
      "name": "door",
      "image": "🚪",
      "category": "Objects"
    },
    {
      "code": "U+1F6D7",
      "name": "elevator",
      "image": "🛗",
      "category": "Objects"
    },
    {
      "code": "U+1FA9E",
      "name": "mirror",
      "image": "🪞",
      "category": "Objects"
    },
    {
      "code": "U+1FA9F",
      "name": "window",
      "image": "🪟",
      "category": "Objects"
    },
    {
      "code": "U+1F6CF",
      "name": "bed",
      "image": "🛏",
      "category": "Objects"
    },
    {
      "code": "U+1F6CB",
      "name": "couch and lamp",
      "image": "🛋",
      "category": "Objects"
    },
    {
      "code": "U+1FA91",
      "name": "chair",
      "image": "🪑",
      "category": "Objects"
    },
    {
      "code": "U+1F6BD",
      "name": "toilet",
      "image": "🚽",
      "category": "Objects"
    },
    {
      "code": "U+1FAA0",
      "name": "plunger",
      "image": "🪠",
      "category": "Objects"
    },
    {
      "code": "U+1F6BF",
      "name": "shower",
      "image": "🚿",
      "category": "Objects"
    },
    {
      "code": "U+1F6C1",
      "name": "bathtub",
      "image": "🛁",
      "category": "Objects"
    },
    {
      "code": "U+1FAA4",
      "name": "mouse trap",
      "image": "🪤",
      "category": "Objects"
    },
    {
      "code": "U+1FA92",
      "name": "razor",
      "image": "🪒",
      "category": "Objects"
    },
    {
      "code": "U+1F9F4",
      "name": "lotion bottle",
      "image": "🧴",
      "category": "Objects"
    },
    {
      "code": "U+1F9F7",
      "name": "safety pin",
      "image": "🧷",
      "category": "Objects"
    },
    {
      "code": "U+1F9F9",
      "name": "broom",
      "image": "🧹",
      "category": "Objects"
    },
    {
      "code": "U+1F9FA",
      "name": "basket",
      "image": "🧺",
      "category": "Objects"
    },
    {
      "code": "U+1F9FB",
      "name": "roll of paper",
      "image": "🧻",
      "category": "Objects"
    },
    {
      "code": "U+1FAA3",
      "name": "bucket",
      "image": "🪣",
      "category": "Objects"
    },
    {
      "code": "U+1F9FC",
      "name": "soap",
      "image": "🧼",
      "category": "Objects"
    },
    {
      "code": "U+1FAE7",
      "name": "bubbles",
      "image": "🫧",
      "category": "Objects"
    },
    {
      "code": "U+1FAA5",
      "name": "toothbrush",
      "image": "🪥",
      "category": "Objects"
    },
    {
      "code": "U+1F9FD",
      "name": "sponge",
      "image": "🧽",
      "category": "Objects"
    },
    {
      "code": "U+1F9EF",
      "name": "fire extinguisher",
      "image": "🧯",
      "category": "Objects"
    },
    {
      "code": "U+1F6D2",
      "name": "shopping cart",
      "image": "🛒",
      "category": "Objects"
    },
    {
      "code": "U+1F6AC",
      "name": "cigarette",
      "image": "🚬",
      "category": "Objects"
    },
    {
      "code": "U+26B0",
      "name": "coffin",
      "image": "⚰",
      "category": "Objects"
    },
    {
      "code": "U+1FAA6",
      "name": "headstone",
      "image": "🪦",
      "category": "Objects"
    },
    {
      "code": "U+26B1",
      "name": "funeral urn",
      "image": "⚱",
      "category": "Objects"
    },
    {
      "code": "U+1F9FF",
      "name": "nazar amulet",
      "image": "🧿",
      "category": "Objects"
    },
    {
      "code": "U+1FAAC",
      "name": "hamsa",
      "image": "🪬",
      "category": "Objects"
    },
    {
      "code": "U+1F5FF",
      "name": "moai",
      "image": "🗿",
      "category": "Objects"
    },
    {
      "code": "U+1FAA7",
      "name": "placard",
      "image": "🪧",
      "category": "Objects"
    },
    {
      "code": "U+1FAAA",
      "name": "identification card",
      "image": "🪪",
      "category": "Objects"
    },  {
      "code": "U+1F3E7",
      "name": "ATM sign",
      "image": "🏧",
      "category": "Symbols"
    },
    {
      "code": "U+1F6AE",
      "name": "litter in bin sign",
      "image": "🚮",
      "category": "Symbols"
    },
    {
      "code": "U+1F6B0",
      "name": "potable water",
      "image": "🚰",
      "category": "Symbols"
    },
    {
      "code": "U+267F",
      "name": "wheelchair symbol",
      "image": "♿",
      "category": "Symbols"
    },
    {
      "code": "U+1F6B9",
      "name": "men’s room",
      "image": "🚹",
      "category": "Symbols"
    },
    {
      "code": "U+1F6BA",
      "name": "women’s room",
      "image": "🚺",
      "category": "Symbols"
    },
    {
      "code": "U+1F6BB",
      "name": "restroom",
      "image": "🚻",
      "category": "Symbols"
    },
    {
      "code": "U+1F6BC",
      "name": "baby symbol",
      "image": "🚼",
      "category": "Symbols"
    },
    {
      "code": "U+1F6BE",
      "name": "water closet",
      "image": "🚾",
      "category": "Symbols"
    },
    {
      "code": "U+1F6C2",
      "name": "passport control",
      "image": "🛂",
      "category": "Symbols"
    },
    {
      "code": "U+1F6C3",
      "name": "customs",
      "image": "🛃",
      "category": "Symbols"
    },
    {
      "code": "U+1F6C4",
      "name": "baggage claim",
      "image": "🛄",
      "category": "Symbols"
    },
    {
      "code": "U+1F6C5",
      "name": "left luggage",
      "image": "🛅",
      "category": "Symbols"
    },
    {
      "code": "U+26A0",
      "name": "warning",
      "image": "⚠",
      "category": "Symbols"
    },
    {
      "code": "U+1F6B8",
      "name": "children crossing",
      "image": "🚸",
      "category": "Symbols"
    },
    {
      "code": "U+26D4",
      "name": "no entry",
      "image": "⛔",
      "category": "Symbols"
    },
    {
      "code": "U+1F6AB",
      "name": "prohibited",
      "image": "🚫",
      "category": "Symbols"
    },
    {
      "code": "U+1F6B3",
      "name": "no bicycles",
      "image": "🚳",
      "category": "Symbols"
    },
    {
      "code": "U+1F6AD",
      "name": "no smoking",
      "image": "🚭",
      "category": "Symbols"
    },
    {
      "code": "U+1F6AF",
      "name": "no littering",
      "image": "🚯",
      "category": "Symbols"
    },
    {
      "code": "U+1F6B1",
      "name": "non-potable water",
      "image": "🚱",
      "category": "Symbols"
    },
    {
      "code": "U+1F6B7",
      "name": "no pedestrians",
      "image": "🚷",
      "category": "Symbols"
    },
    {
      "code": "U+1F4F5",
      "name": "no mobile phones",
      "image": "📵",
      "category": "Symbols"
    },
    {
      "code": "U+1F51E",
      "name": "no one under eighteen",
      "image": "🔞",
      "category": "Symbols"
    },
    {
      "code": "U+2622",
      "name": "radioactive",
      "image": "☢",
      "category": "Symbols"
    },
    {
      "code": "U+2623",
      "name": "biohazard",
      "image": "☣",
      "category": "Symbols"
    },
    {
      "code": "U+2B06",
      "name": "up arrow",
      "image": "⬆",
      "category": "Symbols"
    },
    {
      "code": "U+2197",
      "name": "up-right arrow",
      "image": "↗",
      "category": "Symbols"
    },
    {
      "code": "U+27A1",
      "name": "right arrow",
      "image": "➡",
      "category": "Symbols"
    },
    {
      "code": "U+2198",
      "name": "down-right arrow",
      "image": "↘",
      "category": "Symbols"
    },
    {
      "code": "U+2B07",
      "name": "down arrow",
      "image": "⬇",
      "category": "Symbols"
    },
    {
      "code": "U+2199",
      "name": "down-left arrow",
      "image": "↙",
      "category": "Symbols"
    },
    {
      "code": "U+2B05",
      "name": "left arrow",
      "image": "⬅",
      "category": "Symbols"
    },
    {
      "code": "U+2196",
      "name": "up-left arrow",
      "image": "↖",
      "category": "Symbols"
    },
    {
      "code": "U+2195",
      "name": "up-down arrow",
      "image": "↕",
      "category": "Symbols"
    },
    {
      "code": "U+2194",
      "name": "left-right arrow",
      "image": "↔",
      "category": "Symbols"
    },
    {
      "code": "U+21A9",
      "name": "right arrow curving left",
      "image": "↩",
      "category": "Symbols"
    },
    {
      "code": "U+21AA",
      "name": "left arrow curving right",
      "image": "↪",
      "category": "Symbols"
    },
    {
      "code": "U+2934",
      "name": "right arrow curving up",
      "image": "⤴",
      "category": "Symbols"
    },
    {
      "code": "U+2935",
      "name": "right arrow curving down",
      "image": "⤵",
      "category": "Symbols"
    },
    {
      "code": "U+1F503",
      "name": "clockwise vertical arrows",
      "image": "🔃",
      "category": "Symbols"
    },
    {
      "code": "U+1F504",
      "name": "counterclockwise arrows button",
      "image": "🔄",
      "category": "Symbols"
    },
    {
      "code": "U+1F519",
      "name": "BACK arrow",
      "image": "🔙",
      "category": "Symbols"
    },
    {
      "code": "U+1F51A",
      "name": "END arrow",
      "image": "🔚",
      "category": "Symbols"
    },
    {
      "code": "U+1F51B",
      "name": "ON! arrow",
      "image": "🔛",
      "category": "Symbols"
    },
    {
      "code": "U+1F51C",
      "name": "SOON arrow",
      "image": "🔜",
      "category": "Symbols"
    },
    {
      "code": "U+1F51D",
      "name": "TOP arrow",
      "image": "🔝",
      "category": "Symbols"
    },
    {
      "code": "U+1F6D0",
      "name": "place of worship",
      "image": "🛐",
      "category": "Symbols"
    },
    {
      "code": "U+269B",
      "name": "atom symbol",
      "image": "⚛",
      "category": "Symbols"
    },
    {
      "code": "U+1F549",
      "name": "om",
      "image": "🕉",
      "category": "Symbols"
    },
    {
      "code": "U+2721",
      "name": "star of David",
      "image": "✡",
      "category": "Symbols"
    },
    {
      "code": "U+2638",
      "name": "wheel of dharma",
      "image": "☸",
      "category": "Symbols"
    },
    {
      "code": "U+262F",
      "name": "yin yang",
      "image": "☯",
      "category": "Symbols"
    },
    {
      "code": "U+271D",
      "name": "latin cross",
      "image": "✝",
      "category": "Symbols"
    },
    {
      "code": "U+2626",
      "name": "orthodox cross",
      "image": "☦",
      "category": "Symbols"
    },
    {
      "code": "U+262A",
      "name": "star and crescent",
      "image": "☪",
      "category": "Symbols"
    },
    {
      "code": "U+262E",
      "name": "peace symbol",
      "image": "☮",
      "category": "Symbols"
    },
    {
      "code": "U+1F54E",
      "name": "menorah",
      "image": "🕎",
      "category": "Symbols"
    },
    {
      "code": "U+1F52F",
      "name": "dotted six-pointed star",
      "image": "🔯",
      "category": "Symbols"
    },
    {
      "code": "U+2648",
      "name": "Aries",
      "image": "♈",
      "category": "Symbols"
    },
    {
      "code": "U+2649",
      "name": "Taurus",
      "image": "♉",
      "category": "Symbols"
    },
    {
      "code": "U+264A",
      "name": "Gemini",
      "image": "♊",
      "category": "Symbols"
    },
    {
      "code": "U+264B",
      "name": "Cancer",
      "image": "♋",
      "category": "Symbols"
    },
    {
      "code": "U+264C",
      "name": "Leo",
      "image": "♌",
      "category": "Symbols"
    },
    {
      "code": "U+264D",
      "name": "Virgo",
      "image": "♍",
      "category": "Symbols"
    },
    {
      "code": "U+264E",
      "name": "Libra",
      "image": "♎",
      "category": "Symbols"
    },
    {
      "code": "U+264F",
      "name": "Scorpio",
      "image": "♏",
      "category": "Symbols"
    },
    {
      "code": "U+2650",
      "name": "Sagittarius",
      "image": "♐",
      "category": "Symbols"
    },
    {
      "code": "U+2651",
      "name": "Capricorn",
      "image": "♑",
      "category": "Symbols"
    },
    {
      "code": "U+2652",
      "name": "Aquarius",
      "image": "♒",
      "category": "Symbols"
    },
    {
      "code": "U+2653",
      "name": "Pisces",
      "image": "♓",
      "category": "Symbols"
    },
    {
      "code": "U+26CE",
      "name": "Ophiuchus",
      "image": "⛎",
      "category": "Symbols"
    },
    {
      "code": "U+1F500",
      "name": "shuffle tracks button",
      "image": "🔀",
      "category": "Symbols"
    },
    {
      "code": "U+1F501",
      "name": "repeat button",
      "image": "🔁",
      "category": "Symbols"
    },
    {
      "code": "U+1F502",
      "name": "repeat single button",
      "image": "🔂",
      "category": "Symbols"
    },
    {
      "code": "U+25B6",
      "name": "play button",
      "image": "▶",
      "category": "Symbols"
    },
    {
      "code": "U+23E9",
      "name": "fast-forward button",
      "image": "⏩",
      "category": "Symbols"
    },
    {
      "code": "U+23ED",
      "name": "next track button",
      "image": "⏭",
      "category": "Symbols"
    },
    {
      "code": "U+23EF",
      "name": "play or pause button",
      "image": "⏯",
      "category": "Symbols"
    },
    {
      "code": "U+25C0",
      "name": "reverse button",
      "image": "◀",
      "category": "Symbols"
    },
    {
      "code": "U+23EA",
      "name": "fast reverse button",
      "image": "⏪",
      "category": "Symbols"
    },
    {
      "code": "U+23EE",
      "name": "last track button",
      "image": "⏮",
      "category": "Symbols"
    },
    {
      "code": "U+1F53C",
      "name": "upwards button",
      "image": "🔼",
      "category": "Symbols"
    },
    {
      "code": "U+23EB",
      "name": "fast up button",
      "image": "⏫",
      "category": "Symbols"
    },
    {
      "code": "U+1F53D",
      "name": "downwards button",
      "image": "🔽",
      "category": "Symbols"
    },
    {
      "code": "U+23EC",
      "name": "fast down button",
      "image": "⏬",
      "category": "Symbols"
    },
    {
      "code": "U+23F8",
      "name": "pause button",
      "image": "⏸",
      "category": "Symbols"
    },
    {
      "code": "U+23F9",
      "name": "stop button",
      "image": "⏹",
      "category": "Symbols"
    },
    {
      "code": "U+23FA",
      "name": "record button",
      "image": "⏺",
      "category": "Symbols"
    },
    {
      "code": "U+23CF",
      "name": "eject button",
      "image": "⏏",
      "category": "Symbols"
    },
    {
      "code": "U+1F3A6",
      "name": "cinema",
      "image": "🎦",
      "category": "Symbols"
    },
    {
      "code": "U+1F505",
      "name": "dim button",
      "image": "🔅",
      "category": "Symbols"
    },
    {
      "code": "U+1F506",
      "name": "bright button",
      "image": "🔆",
      "category": "Symbols"
    },
    {
      "code": "U+1F4F6",
      "name": "antenna bars",
      "image": "📶",
      "category": "Symbols"
    },
    {
      "code": "U+1F4F3",
      "name": "vibration mode",
      "image": "📳",
      "category": "Symbols"
    },
    {
      "code": "U+1F4F4",
      "name": "mobile phone off",
      "image": "📴",
      "category": "Symbols"
    },
    {
      "code": "U+2640",
      "name": "female sign",
      "image": "♀",
      "category": "Symbols"
    },
    {
      "code": "U+2642",
      "name": "male sign",
      "image": "♂",
      "category": "Symbols"
    },
    {
      "code": "U+26A7",
      "name": "transgender symbol",
      "image": "⚧",
      "category": "Symbols"
    },
    {
      "code": "U+2716",
      "name": "multiply",
      "image": "✖",
      "category": "Symbols"
    },
    {
      "code": "U+2795",
      "name": "plus",
      "image": "➕",
      "category": "Symbols"
    },
    {
      "code": "U+2796",
      "name": "minus",
      "image": "➖",
      "category": "Symbols"
    },
    {
      "code": "U+2797",
      "name": "divide",
      "image": "➗",
      "category": "Symbols"
    },
    {
      "code": "U+1F7F0",
      "name": "heavy equals sign",
      "image": "🟰",
      "category": "Symbols"
    },
    {
      "code": "U+267E",
      "name": "infinity",
      "image": "♾",
      "category": "Symbols"
    },
    {
      "code": "U+203C",
      "name": "double exclamation mark",
      "image": "‼",
      "category": "Symbols"
    },
    {
      "code": "U+2049",
      "name": "exclamation question mark",
      "image": "⁉",
      "category": "Symbols"
    },
    {
      "code": "U+2753",
      "name": "red question mark",
      "image": "❓",
      "category": "Symbols"
    },
    {
      "code": "U+2754",
      "name": "white question mark",
      "image": "❔",
      "category": "Symbols"
    },
    {
      "code": "U+2755",
      "name": "white exclamation mark",
      "image": "❕",
      "category": "Symbols"
    },
    {
      "code": "U+2757",
      "name": "red exclamation mark",
      "image": "❗",
      "category": "Symbols"
    },
    {
      "code": "U+3030",
      "name": "wavy dash",
      "image": "〰",
      "category": "Symbols"
    },
    {
      "code": "U+1F4B1",
      "name": "currency exchange",
      "image": "💱",
      "category": "Symbols"
    },
    {
      "code": "U+1F4B2",
      "name": "heavy dollar sign",
      "image": "💲",
      "category": "Symbols"
    },
    {
      "code": "U+2695",
      "name": "medical symbol",
      "image": "⚕",
      "category": "Symbols"
    },
    {
      "code": "U+267B",
      "name": "recycling symbol",
      "image": "♻",
      "category": "Symbols"
    },
    {
      "code": "U+269C",
      "name": "fleur-de-lis",
      "image": "⚜",
      "category": "Symbols"
    },
    {
      "code": "U+1F531",
      "name": "trident emblem",
      "image": "🔱",
      "category": "Symbols"
    },
    {
      "code": "U+1F4DB",
      "name": "name badge",
      "image": "📛",
      "category": "Symbols"
    },
    {
      "code": "U+1F530",
      "name": "Japanese symbol for beginner",
      "image": "🔰",
      "category": "Symbols"
    },
    {
      "code": "U+2B55",
      "name": "hollow red circle",
      "image": "⭕",
      "category": "Symbols"
    },
    {
      "code": "U+2705",
      "name": "check mark button",
      "image": "✅",
      "category": "Symbols"
    },
    {
      "code": "U+2611",
      "name": "check box with check",
      "image": "☑",
      "category": "Symbols"
    },
    {
      "code": "U+2714",
      "name": "check mark",
      "image": "✔",
      "category": "Symbols"
    },
    {
      "code": "U+274C",
      "name": "cross mark",
      "image": "❌",
      "category": "Symbols"
    },
    {
      "code": "U+274E",
      "name": "cross mark button",
      "image": "❎",
      "category": "Symbols"
    },
    {
      "code": "U+27B0",
      "name": "curly loop",
      "image": "➰",
      "category": "Symbols"
    },
    {
      "code": "U+27BF",
      "name": "double curly loop",
      "image": "➿",
      "category": "Symbols"
    },
    {
      "code": "U+303D",
      "name": "part alternation mark",
      "image": "〽",
      "category": "Symbols"
    },
    {
      "code": "U+2733",
      "name": "eight-spoked asterisk",
      "image": "✳",
      "category": "Symbols"
    },
    {
      "code": "U+2734",
      "name": "eight-pointed star",
      "image": "✴",
      "category": "Symbols"
    },
    {
      "code": "U+2747",
      "name": "sparkle",
      "image": "❇",
      "category": "Symbols"
    },
    {
      "code": "U+00A9",
      "name": "copyright",
      "image": "©",
      "category": "Symbols"
    },
    {
      "code": "U+00AE",
      "name": "registered",
      "image": "®",
      "category": "Symbols"
    },
    {
      "code": "U+2122",
      "name": "trade mark",
      "image": "™",
      "category": "Symbols"
    },
    {
      "code": "U+0023 U+FE0F U+20E3",
      "name": "keycap: #",
      "image": "#️⃣",
      "category": "Symbols"
    },
    {
      "code": "U+002A U+FE0F U+20E3",
      "name": "keycap: *",
      "image": "*️⃣",
      "category": "Symbols"
    },
    {
      "code": "U+0030 U+FE0F U+20E3",
      "name": "keycap: 0",
      "image": "0️⃣",
      "category": "Symbols"
    },
    {
      "code": "U+0031 U+FE0F U+20E3",
      "name": "keycap: 1",
      "image": "1️⃣",
      "category": "Symbols"
    },
    {
      "code": "U+0032 U+FE0F U+20E3",
      "name": "keycap: 2",
      "image": "2️⃣",
      "category": "Symbols"
    },
    {
      "code": "U+0033 U+FE0F U+20E3",
      "name": "keycap: 3",
      "image": "3️⃣",
      "category": "Symbols"
    },
    {
      "code": "U+0034 U+FE0F U+20E3",
      "name": "keycap: 4",
      "image": "4️⃣",
      "category": "Symbols"
    },
    {
      "code": "U+0035 U+FE0F U+20E3",
      "name": "keycap: 5",
      "image": "5️⃣",
      "category": "Symbols"
    },
    {
      "code": "U+0036 U+FE0F U+20E3",
      "name": "keycap: 6",
      "image": "6️⃣",
      "category": "Symbols"
    },
    {
      "code": "U+0037 U+FE0F U+20E3",
      "name": "keycap: 7",
      "image": "7️⃣",
      "category": "Symbols"
    },
    {
      "code": "U+0038 U+FE0F U+20E3",
      "name": "keycap: 8",
      "image": "8️⃣",
      "category": "Symbols"
    },
    {
      "code": "U+0039 U+FE0F U+20E3",
      "name": "keycap: 9",
      "image": "9️⃣",
      "category": "Symbols"
    },
    {
      "code": "U+1F51F",
      "name": "keycap: 10",
      "image": "🔟",
      "category": "Symbols"
    },
    {
      "code": "U+1F520",
      "name": "input latin uppercase",
      "image": "🔠",
      "category": "Symbols"
    },
    {
      "code": "U+1F521",
      "name": "input latin lowercase",
      "image": "🔡",
      "category": "Symbols"
    },
    {
      "code": "U+1F522",
      "name": "input numbers",
      "image": "🔢",
      "category": "Symbols"
    },
    {
      "code": "U+1F523",
      "name": "input symbols",
      "image": "🔣",
      "category": "Symbols"
    },
    {
      "code": "U+1F524",
      "name": "input latin letters",
      "image": "🔤",
      "category": "Symbols"
    },
    {
      "code": "U+1F170",
      "name": "A button (blood type)",
      "image": "🅰",
      "category": "Symbols"
    },
    {
      "code": "U+1F18E",
      "name": "AB button (blood type)",
      "image": "🆎",
      "category": "Symbols"
    },
    {
      "code": "U+1F171",
      "name": "B button (blood type)",
      "image": "🅱",
      "category": "Symbols"
    },
    {
      "code": "U+1F191",
      "name": "CL button",
      "image": "🆑",
      "category": "Symbols"
    },
    {
      "code": "U+1F192",
      "name": "COOL button",
      "image": "🆒",
      "category": "Symbols"
    },
    {
      "code": "U+1F193",
      "name": "FREE button",
      "image": "🆓",
      "category": "Symbols"
    },
    {
      "code": "U+2139",
      "name": "information",
      "image": "ℹ",
      "category": "Symbols"
    },
    {
      "code": "U+1F194",
      "name": "ID button",
      "image": "🆔",
      "category": "Symbols"
    },
    {
      "code": "U+24C2",
      "name": "circled M",
      "image": "Ⓜ",
      "category": "Symbols"
    },
    {
      "code": "U+1F195",
      "name": "NEW button",
      "image": "🆕",
      "category": "Symbols"
    },
    {
      "code": "U+1F196",
      "name": "NG button",
      "image": "🆖",
      "category": "Symbols"
    },
    {
      "code": "U+1F17E",
      "name": "O button (blood type)",
      "image": "🅾",
      "category": "Symbols"
    },
    {
      "code": "U+1F197",
      "name": "OK button",
      "image": "🆗",
      "category": "Symbols"
    },
    {
      "code": "U+1F17F",
      "name": "P button",
      "image": "🅿",
      "category": "Symbols"
    },
    {
      "code": "U+1F198",
      "name": "SOS button",
      "image": "🆘",
      "category": "Symbols"
    },
    {
      "code": "U+1F199",
      "name": "UP! button",
      "image": "🆙",
      "category": "Symbols"
    },
    {
      "code": "U+1F19A",
      "name": "VS button",
      "image": "🆚",
      "category": "Symbols"
    },
    {
      "code": "U+1F201",
      "name": "Japanese “here” button",
      "image": "🈁",
      "category": "Symbols"
    },
    {
      "code": "U+1F202",
      "name": "Japanese “service charge” button",
      "image": "🈂",
      "category": "Symbols"
    },
    {
      "code": "U+1F237",
      "name": "Japanese “monthly amount” button",
      "image": "🈷",
      "category": "Symbols"
    },
    {
      "code": "U+1F236",
      "name": "Japanese “not free of charge” button",
      "image": "🈶",
      "category": "Symbols"
    },
    {
      "code": "U+1F22F",
      "name": "Japanese “reserved” button",
      "image": "🈯",
      "category": "Symbols"
    },
    {
      "code": "U+1F250",
      "name": "Japanese “bargain” button",
      "image": "🉐",
      "category": "Symbols"
    },
    {
      "code": "U+1F239",
      "name": "Japanese “discount” button",
      "image": "🈹",
      "category": "Symbols"
    },
    {
      "code": "U+1F21A",
      "name": "Japanese “free of charge” button",
      "image": "🈚",
      "category": "Symbols"
    },
    {
      "code": "U+1F232",
      "name": "Japanese “prohibited” button",
      "image": "🈲",
      "category": "Symbols"
    },
    {
      "code": "U+1F251",
      "name": "Japanese “acceptable” button",
      "image": "🉑",
      "category": "Symbols"
    },
    {
      "code": "U+1F238",
      "name": "Japanese “application” button",
      "image": "🈸",
      "category": "Symbols"
    },
    {
      "code": "U+1F234",
      "name": "Japanese “passing grade” button",
      "image": "🈴",
      "category": "Symbols"
    },
    {
      "code": "U+1F233",
      "name": "Japanese “vacancy” button",
      "image": "🈳",
      "category": "Symbols"
    },
    {
      "code": "U+3297",
      "name": "Japanese “congratulations” button",
      "image": "㊗",
      "category": "Symbols"
    },
    {
      "code": "U+3299",
      "name": "Japanese “secret” button",
      "image": "㊙",
      "category": "Symbols"
    },
    {
      "code": "U+1F23A",
      "name": "Japanese “open for business” button",
      "image": "🈺",
      "category": "Symbols"
    },
    {
      "code": "U+1F235",
      "name": "Japanese “no vacancy” button",
      "image": "🈵",
      "category": "Symbols"
    },
    {
      "code": "U+1F534",
      "name": "red circle",
      "image": "🔴",
      "category": "Symbols"
    },
    {
      "code": "U+1F7E0",
      "name": "orange circle",
      "image": "🟠",
      "category": "Symbols"
    },
    {
      "code": "U+1F7E1",
      "name": "yellow circle",
      "image": "🟡",
      "category": "Symbols"
    },
    {
      "code": "U+1F7E2",
      "name": "green circle",
      "image": "🟢",
      "category": "Symbols"
    },
    {
      "code": "U+1F535",
      "name": "blue circle",
      "image": "🔵",
      "category": "Symbols"
    },
    {
      "code": "U+1F7E3",
      "name": "purple circle",
      "image": "🟣",
      "category": "Symbols"
    },
    {
      "code": "U+1F7E4",
      "name": "brown circle",
      "image": "🟤",
      "category": "Symbols"
    },
    {
      "code": "U+26AB",
      "name": "black circle",
      "image": "⚫",
      "category": "Symbols"
    },
    {
      "code": "U+26AA",
      "name": "white circle",
      "image": "⚪",
      "category": "Symbols"
    },
    {
      "code": "U+1F7E5",
      "name": "red square",
      "image": "🟥",
      "category": "Symbols"
    },
    {
      "code": "U+1F7E7",
      "name": "orange square",
      "image": "🟧",
      "category": "Symbols"
    },
    {
      "code": "U+1F7E8",
      "name": "yellow square",
      "image": "🟨",
      "category": "Symbols"
    },
    {
      "code": "U+1F7E9",
      "name": "green square",
      "image": "🟩",
      "category": "Symbols"
    },
    {
      "code": "U+1F7E6",
      "name": "blue square",
      "image": "🟦",
      "category": "Symbols"
    },
    {
      "code": "U+1F7EA",
      "name": "purple square",
      "image": "🟪",
      "category": "Symbols"
    },
    {
      "code": "U+1F7EB",
      "name": "brown square",
      "image": "🟫",
      "category": "Symbols"
    },
    {
      "code": "U+2B1B",
      "name": "black large square",
      "image": "⬛",
      "category": "Symbols"
    },
    {
      "code": "U+2B1C",
      "name": "white large square",
      "image": "⬜",
      "category": "Symbols"
    },
    {
      "code": "U+25FC",
      "name": "black medium square",
      "image": "◼",
      "category": "Symbols"
    },
    {
      "code": "U+25FB",
      "name": "white medium square",
      "image": "◻",
      "category": "Symbols"
    },
    {
      "code": "U+25FE",
      "name": "black medium-small square",
      "image": "◾",
      "category": "Symbols"
    },
    {
      "code": "U+25FD",
      "name": "white medium-small square",
      "image": "◽",
      "category": "Symbols"
    },
    {
      "code": "U+25AA",
      "name": "black small square",
      "image": "▪",
      "category": "Symbols"
    },
    {
      "code": "U+25AB",
      "name": "white small square",
      "image": "▫",
      "category": "Symbols"
    },
    {
      "code": "U+1F536",
      "name": "large orange diamond",
      "image": "🔶",
      "category": "Symbols"
    },
    {
      "code": "U+1F537",
      "name": "large blue diamond",
      "image": "🔷",
      "category": "Symbols"
    },
    {
      "code": "U+1F538",
      "name": "small orange diamond",
      "image": "🔸",
      "category": "Symbols"
    },
    {
      "code": "U+1F539",
      "name": "small blue diamond",
      "image": "🔹",
      "category": "Symbols"
    },
    {
      "code": "U+1F53A",
      "name": "red triangle pointed up",
      "image": "🔺",
      "category": "Symbols"
    },
    {
      "code": "U+1F53B",
      "name": "red triangle pointed down",
      "image": "🔻",
      "category": "Symbols"
    },
    {
      "code": "U+1F4A0",
      "name": "diamond with a dot",
      "image": "💠",
      "category": "Symbols"
    },
    {
      "code": "U+1F518",
      "name": "radio button",
      "image": "🔘",
      "category": "Symbols"
    },
    {
      "code": "U+1F533",
      "name": "white square button",
      "image": "🔳",
      "category": "Symbols"
    },
    {
      "code": "U+1F532",
      "name": "black square button",
      "image": "🔲",
      "category": "Symbols"
    },{
      "code": "U+1F3C1",
      "name": "chequered flag",
      "image": "🏁",
      "category": "Flags"
    },
    {
      "code": "U+1F6A9",
      "name": "triangular flag",
      "image": "🚩",
      "category": "Flags"
    },
    {
      "code": "U+1F38C",
      "name": "crossed flags",
      "image": "🎌",
      "category": "Flags"
    },
    {
      "code": "U+1F3F4",
      "name": "black flag",
      "image": "🏴",
      "category": "Flags"
    },
    {
      "code": "U+1F3F3",
      "name": "white flag",
      "image": "🏳",
      "category": "Flags"
    },
    {
      "code": "U+1F3F3 U+FE0F U+200D U+1F308",
      "name": "rainbow flag",
      "image": "🏳️‍🌈",
      "category": "Flags"
    },
    {
      "code": "U+1F3F3 U+FE0F U+200D U+26A7 U+FE0F",
      "name": "transgender flag",
      "image": "🏳️‍⚧️",
      "category": "Flags"
    },
    {
      "code": "U+1F3F4 U+200D U+2620 U+FE0F",
      "name": "pirate flag",
      "image": "🏴‍☠️",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1E8",
      "name": "flag: Ascension Island",
      "image": "🇦🇨",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1E9",
      "name": "flag: Andorra",
      "image": "🇦🇩",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1EA",
      "name": "flag: United Arab Emirates",
      "image": "🇦🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1EB",
      "name": "flag: Afghanistan",
      "image": "🇦🇫",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1EC",
      "name": "flag: Antigua & Barbuda",
      "image": "🇦🇬",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1EE",
      "name": "flag: Anguilla",
      "image": "🇦🇮",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1F1",
      "name": "flag: Albania",
      "image": "🇦🇱",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1F2",
      "name": "flag: Armenia",
      "image": "🇦🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1F4",
      "name": "flag: Angola",
      "image": "🇦🇴",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1F6",
      "name": "flag: Antarctica",
      "image": "🇦🇶",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1F7",
      "name": "flag: Argentina",
      "image": "🇦🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1F8",
      "name": "flag: American Samoa",
      "image": "🇦🇸",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1F9",
      "name": "flag: Austria",
      "image": "🇦🇹",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1FA",
      "name": "flag: Australia",
      "image": "🇦🇺",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1FC",
      "name": "flag: Aruba",
      "image": "🇦🇼",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1FD",
      "name": "flag: Åland Islands",
      "image": "🇦🇽",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1FF",
      "name": "flag: Azerbaijan",
      "image": "🇦🇿",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1E6",
      "name": "flag: Bosnia & Herzegovina",
      "image": "🇧🇦",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1E7",
      "name": "flag: Barbados",
      "image": "🇧🇧",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1E9",
      "name": "flag: Bangladesh",
      "image": "🇧🇩",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1EA",
      "name": "flag: Belgium",
      "image": "🇧🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1EB",
      "name": "flag: Burkina Faso",
      "image": "🇧🇫",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1EC",
      "name": "flag: Bulgaria",
      "image": "🇧🇬",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1ED",
      "name": "flag: Bahrain",
      "image": "🇧🇭",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1EE",
      "name": "flag: Burundi",
      "image": "🇧🇮",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1EF",
      "name": "flag: Benin",
      "image": "🇧🇯",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1F1",
      "name": "flag: St. Barthélemy",
      "image": "🇧🇱",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1F2",
      "name": "flag: Bermuda",
      "image": "🇧🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1F3",
      "name": "flag: Brunei",
      "image": "🇧🇳",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1F4",
      "name": "flag: Bolivia",
      "image": "🇧🇴",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1F6",
      "name": "flag: Caribbean Netherlands",
      "image": "🇧🇶",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1F7",
      "name": "flag: Brazil",
      "image": "🇧🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1F8",
      "name": "flag: Bahamas",
      "image": "🇧🇸",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1F9",
      "name": "flag: Bhutan",
      "image": "🇧🇹",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1FB",
      "name": "flag: Bouvet Island",
      "image": "🇧🇻",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1FC",
      "name": "flag: Botswana",
      "image": "🇧🇼",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1FE",
      "name": "flag: Belarus",
      "image": "🇧🇾",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1FF",
      "name": "flag: Belize",
      "image": "🇧🇿",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1E6",
      "name": "flag: Canada",
      "image": "🇨🇦",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1E8",
      "name": "flag: Cocos (Keeling) Islands",
      "image": "🇨🇨",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1E9",
      "name": "flag: Congo - Kinshasa",
      "image": "🇨🇩",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1EB",
      "name": "flag: Central African Republic",
      "image": "🇨🇫",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1EC",
      "name": "flag: Congo - Brazzaville",
      "image": "🇨🇬",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1ED",
      "name": "flag: Switzerland",
      "image": "🇨🇭",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1EE",
      "name": "flag: Côte d’Ivoire",
      "image": "🇨🇮",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1F0",
      "name": "flag: Cook Islands",
      "image": "🇨🇰",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1F1",
      "name": "flag: Chile",
      "image": "🇨🇱",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1F2",
      "name": "flag: Cameroon",
      "image": "🇨🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1F3",
      "name": "flag: China",
      "image": "🇨🇳",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1F4",
      "name": "flag: Colombia",
      "image": "🇨🇴",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1F5",
      "name": "flag: Clipperton Island",
      "image": "🇨🇵",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1F7",
      "name": "flag: Costa Rica",
      "image": "🇨🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1FA",
      "name": "flag: Cuba",
      "image": "🇨🇺",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1FB",
      "name": "flag: Cape Verde",
      "image": "🇨🇻",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1FC",
      "name": "flag: Curaçao",
      "image": "🇨🇼",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1FD",
      "name": "flag: Christmas Island",
      "image": "🇨🇽",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1FE",
      "name": "flag: Cyprus",
      "image": "🇨🇾",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1FF",
      "name": "flag: Czechia",
      "image": "🇨🇿",
      "category": "Flags"
    },
    {
      "code": "U+1F1E9 U+1F1EA",
      "name": "flag: Germany",
      "image": "🇩🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1E9 U+1F1EC",
      "name": "flag: Diego Garcia",
      "image": "🇩🇬",
      "category": "Flags"
    },
    {
      "code": "U+1F1E9 U+1F1EF",
      "name": "flag: Djibouti",
      "image": "🇩🇯",
      "category": "Flags"
    },
    {
      "code": "U+1F1E9 U+1F1F0",
      "name": "flag: Denmark",
      "image": "🇩🇰",
      "category": "Flags"
    },
    {
      "code": "U+1F1E9 U+1F1F2",
      "name": "flag: Dominica",
      "image": "🇩🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1E9 U+1F1F4",
      "name": "flag: Dominican Republic",
      "image": "🇩🇴",
      "category": "Flags"
    },
    {
      "code": "U+1F1E9 U+1F1FF",
      "name": "flag: Algeria",
      "image": "🇩🇿",
      "category": "Flags"
    },
    {
      "code": "U+1F1EA U+1F1E6",
      "name": "flag: Ceuta & Melilla",
      "image": "🇪🇦",
      "category": "Flags"
    },
    {
      "code": "U+1F1EA U+1F1E8",
      "name": "flag: Ecuador",
      "image": "🇪🇨",
      "category": "Flags"
    },
    {
      "code": "U+1F1EA U+1F1EA",
      "name": "flag: Estonia",
      "image": "🇪🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1EA U+1F1EC",
      "name": "flag: Egypt",
      "image": "🇪🇬",
      "category": "Flags"
    },
    {
      "code": "U+1F1EA U+1F1ED",
      "name": "flag: Western Sahara",
      "image": "🇪🇭",
      "category": "Flags"
    },
    {
      "code": "U+1F1EA U+1F1F7",
      "name": "flag: Eritrea",
      "image": "🇪🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1EA U+1F1F8",
      "name": "flag: Spain",
      "image": "🇪🇸",
      "category": "Flags"
    },
    {
      "code": "U+1F1EA U+1F1F9",
      "name": "flag: Ethiopia",
      "image": "🇪🇹",
      "category": "Flags"
    },
    {
      "code": "U+1F1EA U+1F1FA",
      "name": "flag: European Union",
      "image": "🇪🇺",
      "category": "Flags"
    },
    {
      "code": "U+1F1EB U+1F1EE",
      "name": "flag: Finland",
      "image": "🇫🇮",
      "category": "Flags"
    },
    {
      "code": "U+1F1EB U+1F1EF",
      "name": "flag: Fiji",
      "image": "🇫🇯",
      "category": "Flags"
    },
    {
      "code": "U+1F1EB U+1F1F0",
      "name": "flag: Falkland Islands",
      "image": "🇫🇰",
      "category": "Flags"
    },
    {
      "code": "U+1F1EB U+1F1F2",
      "name": "flag: Micronesia",
      "image": "🇫🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1EB U+1F1F4",
      "name": "flag: Faroe Islands",
      "image": "🇫🇴",
      "category": "Flags"
    },
    {
      "code": "U+1F1EB U+1F1F7",
      "name": "flag: France",
      "image": "🇫🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1E6",
      "name": "flag: Gabon",
      "image": "🇬🇦",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1E7",
      "name": "flag: United Kingdom",
      "image": "🇬🇧",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1E9",
      "name": "flag: Grenada",
      "image": "🇬🇩",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1EA",
      "name": "flag: Georgia",
      "image": "🇬🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1EB",
      "name": "flag: French Guiana",
      "image": "🇬🇫",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1EC",
      "name": "flag: Guernsey",
      "image": "🇬🇬",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1ED",
      "name": "flag: Ghana",
      "image": "🇬🇭",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1EE",
      "name": "flag: Gibraltar",
      "image": "🇬🇮",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1F1",
      "name": "flag: Greenland",
      "image": "🇬🇱",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1F2",
      "name": "flag: Gambia",
      "image": "🇬🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1F3",
      "name": "flag: Guinea",
      "image": "🇬🇳",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1F5",
      "name": "flag: Guadeloupe",
      "image": "🇬🇵",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1F6",
      "name": "flag: Equatorial Guinea",
      "image": "🇬🇶",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1F7",
      "name": "flag: Greece",
      "image": "🇬🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1F8",
      "name": "flag: South Georgia & South Sandwich Islands",
      "image": "🇬🇸",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1F9",
      "name": "flag: Guatemala",
      "image": "🇬🇹",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1FA",
      "name": "flag: Guam",
      "image": "🇬🇺",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1FC",
      "name": "flag: Guinea-Bissau",
      "image": "🇬🇼",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1FE",
      "name": "flag: Guyana",
      "image": "🇬🇾",
      "category": "Flags"
    },
    {
      "code": "U+1F1ED U+1F1F0",
      "name": "flag: Hong Kong SAR China",
      "image": "🇭🇰",
      "category": "Flags"
    },
    {
      "code": "U+1F1ED U+1F1F2",
      "name": "flag: Heard & McDonald Islands",
      "image": "🇭🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1ED U+1F1F3",
      "name": "flag: Honduras",
      "image": "🇭🇳",
      "category": "Flags"
    },
    {
      "code": "U+1F1ED U+1F1F7",
      "name": "flag: Croatia",
      "image": "🇭🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1ED U+1F1F9",
      "name": "flag: Haiti",
      "image": "🇭🇹",
      "category": "Flags"
    },
    {
      "code": "U+1F1ED U+1F1FA",
      "name": "flag: Hungary",
      "image": "🇭🇺",
      "category": "Flags"
    },
    {
      "code": "U+1F1EE U+1F1E8",
      "name": "flag: Canary Islands",
      "image": "🇮🇨",
      "category": "Flags"
    },
    {
      "code": "U+1F1EE U+1F1E9",
      "name": "flag: Indonesia",
      "image": "🇮🇩",
      "category": "Flags"
    },
    {
      "code": "U+1F1EE U+1F1EA",
      "name": "flag: Ireland",
      "image": "🇮🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1EE U+1F1F1",
      "name": "flag: Israel",
      "image": "🇮🇱",
      "category": "Flags"
    },
    {
      "code": "U+1F1EE U+1F1F2",
      "name": "flag: Isle of Man",
      "image": "🇮🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1EE U+1F1F3",
      "name": "flag: India",
      "image": "🇮🇳",
      "category": "Flags"
    },
    {
      "code": "U+1F1EE U+1F1F4",
      "name": "flag: British Indian Ocean Territory",
      "image": "🇮🇴",
      "category": "Flags"
    },
    {
      "code": "U+1F1EE U+1F1F6",
      "name": "flag: Iraq",
      "image": "🇮🇶",
      "category": "Flags"
    },
    {
      "code": "U+1F1EE U+1F1F7",
      "name": "flag: Iran",
      "image": "🇮🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1EE U+1F1F8",
      "name": "flag: Iceland",
      "image": "🇮🇸",
      "category": "Flags"
    },
    {
      "code": "U+1F1EE U+1F1F9",
      "name": "flag: Italy",
      "image": "🇮🇹",
      "category": "Flags"
    },
    {
      "code": "U+1F1EF U+1F1EA",
      "name": "flag: Jersey",
      "image": "🇯🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1EF U+1F1F2",
      "name": "flag: Jamaica",
      "image": "🇯🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1EF U+1F1F4",
      "name": "flag: Jordan",
      "image": "🇯🇴",
      "category": "Flags"
    },
    {
      "code": "U+1F1EF U+1F1F5",
      "name": "flag: Japan",
      "image": "🇯🇵",
      "category": "Flags"
    },
    {
      "code": "U+1F1F0 U+1F1EA",
      "name": "flag: Kenya",
      "image": "🇰🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1F0 U+1F1EC",
      "name": "flag: Kyrgyzstan",
      "image": "🇰🇬",
      "category": "Flags"
    },
    {
      "code": "U+1F1F0 U+1F1ED",
      "name": "flag: Cambodia",
      "image": "🇰🇭",
      "category": "Flags"
    },
    {
      "code": "U+1F1F0 U+1F1EE",
      "name": "flag: Kiribati",
      "image": "🇰🇮",
      "category": "Flags"
    },
    {
      "code": "U+1F1F0 U+1F1F2",
      "name": "flag: Comoros",
      "image": "🇰🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1F0 U+1F1F3",
      "name": "flag: St. Kitts & Nevis",
      "image": "🇰🇳",
      "category": "Flags"
    },
    {
      "code": "U+1F1F0 U+1F1F5",
      "name": "flag: North Korea",
      "image": "🇰🇵",
      "category": "Flags"
    },
    {
      "code": "U+1F1F0 U+1F1F7",
      "name": "flag: South Korea",
      "image": "🇰🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1F0 U+1F1FC",
      "name": "flag: Kuwait",
      "image": "🇰🇼",
      "category": "Flags"
    },
    {
      "code": "U+1F1F0 U+1F1FE",
      "name": "flag: Cayman Islands",
      "image": "🇰🇾",
      "category": "Flags"
    },
    {
      "code": "U+1F1F0 U+1F1FF",
      "name": "flag: Kazakhstan",
      "image": "🇰🇿",
      "category": "Flags"
    },
    {
      "code": "U+1F1F1 U+1F1E6",
      "name": "flag: Laos",
      "image": "🇱🇦",
      "category": "Flags"
    },
    {
      "code": "U+1F1F1 U+1F1E7",
      "name": "flag: Lebanon",
      "image": "🇱🇧",
      "category": "Flags"
    },
    {
      "code": "U+1F1F1 U+1F1E8",
      "name": "flag: St. Lucia",
      "image": "🇱🇨",
      "category": "Flags"
    },
    {
      "code": "U+1F1F1 U+1F1EE",
      "name": "flag: Liechtenstein",
      "image": "🇱🇮",
      "category": "Flags"
    },
    {
      "code": "U+1F1F1 U+1F1F0",
      "name": "flag: Sri Lanka",
      "image": "🇱🇰",
      "category": "Flags"
    },
    {
      "code": "U+1F1F1 U+1F1F7",
      "name": "flag: Liberia",
      "image": "🇱🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1F1 U+1F1F8",
      "name": "flag: Lesotho",
      "image": "🇱🇸",
      "category": "Flags"
    },
    {
      "code": "U+1F1F1 U+1F1F9",
      "name": "flag: Lithuania",
      "image": "🇱🇹",
      "category": "Flags"
    },
    {
      "code": "U+1F1F1 U+1F1FA",
      "name": "flag: Luxembourg",
      "image": "🇱🇺",
      "category": "Flags"
    },
    {
      "code": "U+1F1F1 U+1F1FB",
      "name": "flag: Latvia",
      "image": "🇱🇻",
      "category": "Flags"
    },
    {
      "code": "U+1F1F1 U+1F1FE",
      "name": "flag: Libya",
      "image": "🇱🇾",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1E6",
      "name": "flag: Morocco",
      "image": "🇲🇦",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1E8",
      "name": "flag: Monaco",
      "image": "🇲🇨",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1E9",
      "name": "flag: Moldova",
      "image": "🇲🇩",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1EA",
      "name": "flag: Montenegro",
      "image": "🇲🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1EB",
      "name": "flag: St. Martin",
      "image": "🇲🇫",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1EC",
      "name": "flag: Madagascar",
      "image": "🇲🇬",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1ED",
      "name": "flag: Marshall Islands",
      "image": "🇲🇭",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1F0",
      "name": "flag: North Macedonia",
      "image": "🇲🇰",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1F1",
      "name": "flag: Mali",
      "image": "🇲🇱",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1F2",
      "name": "flag: Myanmar (Burma)",
      "image": "🇲🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1F3",
      "name": "flag: Mongolia",
      "image": "🇲🇳",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1F4",
      "name": "flag: Macao SAR China",
      "image": "🇲🇴",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1F5",
      "name": "flag: Northern Mariana Islands",
      "image": "🇲🇵",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1F6",
      "name": "flag: Martinique",
      "image": "🇲🇶",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1F7",
      "name": "flag: Mauritania",
      "image": "🇲🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1F8",
      "name": "flag: Montserrat",
      "image": "🇲🇸",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1F9",
      "name": "flag: Malta",
      "image": "🇲🇹",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1FA",
      "name": "flag: Mauritius",
      "image": "🇲🇺",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1FB",
      "name": "flag: Maldives",
      "image": "🇲🇻",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1FC",
      "name": "flag: Malawi",
      "image": "🇲🇼",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1FD",
      "name": "flag: Mexico",
      "image": "🇲🇽",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1FE",
      "name": "flag: Malaysia",
      "image": "🇲🇾",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1FF",
      "name": "flag: Mozambique",
      "image": "🇲🇿",
      "category": "Flags"
    },
    {
      "code": "U+1F1F3 U+1F1E6",
      "name": "flag: Namibia",
      "image": "🇳🇦",
      "category": "Flags"
    },
    {
      "code": "U+1F1F3 U+1F1E8",
      "name": "flag: New Caledonia",
      "image": "🇳🇨",
      "category": "Flags"
    },
    {
      "code": "U+1F1F3 U+1F1EA",
      "name": "flag: Niger",
      "image": "🇳🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1F3 U+1F1EB",
      "name": "flag: Norfolk Island",
      "image": "🇳🇫",
      "category": "Flags"
    },
    {
      "code": "U+1F1F3 U+1F1EC",
      "name": "flag: Nigeria",
      "image": "🇳🇬",
      "category": "Flags"
    },
    {
      "code": "U+1F1F3 U+1F1EE",
      "name": "flag: Nicaragua",
      "image": "🇳🇮",
      "category": "Flags"
    },
    {
      "code": "U+1F1F3 U+1F1F1",
      "name": "flag: Netherlands",
      "image": "🇳🇱",
      "category": "Flags"
    },
    {
      "code": "U+1F1F3 U+1F1F4",
      "name": "flag: Norway",
      "image": "🇳🇴",
      "category": "Flags"
    },
    {
      "code": "U+1F1F3 U+1F1F5",
      "name": "flag: Nepal",
      "image": "🇳🇵",
      "category": "Flags"
    },
    {
      "code": "U+1F1F3 U+1F1F7",
      "name": "flag: Nauru",
      "image": "🇳🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1F3 U+1F1FA",
      "name": "flag: Niue",
      "image": "🇳🇺",
      "category": "Flags"
    },
    {
      "code": "U+1F1F3 U+1F1FF",
      "name": "flag: New Zealand",
      "image": "🇳🇿",
      "category": "Flags"
    },
    {
      "code": "U+1F1F4 U+1F1F2",
      "name": "flag: Oman",
      "image": "🇴🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1F5 U+1F1E6",
      "name": "flag: Panama",
      "image": "🇵🇦",
      "category": "Flags"
    },
    {
      "code": "U+1F1F5 U+1F1EA",
      "name": "flag: Peru",
      "image": "🇵🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1F5 U+1F1EB",
      "name": "flag: French Polynesia",
      "image": "🇵🇫",
      "category": "Flags"
    },
    {
      "code": "U+1F1F5 U+1F1EC",
      "name": "flag: Papua New Guinea",
      "image": "🇵🇬",
      "category": "Flags"
    },
    {
      "code": "U+1F1F5 U+1F1ED",
      "name": "flag: Philippines",
      "image": "🇵🇭",
      "category": "Flags"
    },
    {
      "code": "U+1F1F5 U+1F1F0",
      "name": "flag: Pakistan",
      "image": "🇵🇰",
      "category": "Flags"
    },
    {
      "code": "U+1F1F5 U+1F1F1",
      "name": "flag: Poland",
      "image": "🇵🇱",
      "category": "Flags"
    },
    {
      "code": "U+1F1F5 U+1F1F2",
      "name": "flag: St. Pierre & Miquelon",
      "image": "🇵🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1F5 U+1F1F3",
      "name": "flag: Pitcairn Islands",
      "image": "🇵🇳",
      "category": "Flags"
    },
    {
      "code": "U+1F1F5 U+1F1F7",
      "name": "flag: Puerto Rico",
      "image": "🇵🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1F5 U+1F1F8",
      "name": "flag: Palestinian Territories",
      "image": "🇵🇸",
      "category": "Flags"
    },
    {
      "code": "U+1F1F5 U+1F1F9",
      "name": "flag: Portugal",
      "image": "🇵🇹",
      "category": "Flags"
    },
    {
      "code": "U+1F1F5 U+1F1FC",
      "name": "flag: Palau",
      "image": "🇵🇼",
      "category": "Flags"
    },
    {
      "code": "U+1F1F5 U+1F1FE",
      "name": "flag: Paraguay",
      "image": "🇵🇾",
      "category": "Flags"
    },
    {
      "code": "U+1F1F6 U+1F1E6",
      "name": "flag: Qatar",
      "image": "🇶🇦",
      "category": "Flags"
    },
    {
      "code": "U+1F1F7 U+1F1EA",
      "name": "flag: Réunion",
      "image": "🇷🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1F7 U+1F1F4",
      "name": "flag: Romania",
      "image": "🇷🇴",
      "category": "Flags"
    },
    {
      "code": "U+1F1F7 U+1F1F8",
      "name": "flag: Serbia",
      "image": "🇷🇸",
      "category": "Flags"
    },
    {
      "code": "U+1F1F7 U+1F1FA",
      "name": "flag: Russia",
      "image": "🇷🇺",
      "category": "Flags"
    },
    {
      "code": "U+1F1F7 U+1F1FC",
      "name": "flag: Rwanda",
      "image": "🇷🇼",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1E6",
      "name": "flag: Saudi Arabia",
      "image": "🇸🇦",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1E7",
      "name": "flag: Solomon Islands",
      "image": "🇸🇧",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1E8",
      "name": "flag: Seychelles",
      "image": "🇸🇨",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1E9",
      "name": "flag: Sudan",
      "image": "🇸🇩",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1EA",
      "name": "flag: Sweden",
      "image": "🇸🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1EC",
      "name": "flag: Singapore",
      "image": "🇸🇬",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1ED",
      "name": "flag: St. Helena",
      "image": "🇸🇭",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1EE",
      "name": "flag: Slovenia",
      "image": "🇸🇮",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1EF",
      "name": "flag: Svalbard & Jan Mayen",
      "image": "🇸🇯",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1F0",
      "name": "flag: Slovakia",
      "image": "🇸🇰",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1F1",
      "name": "flag: Sierra Leone",
      "image": "🇸🇱",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1F2",
      "name": "flag: San Marino",
      "image": "🇸🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1F3",
      "name": "flag: Senegal",
      "image": "🇸🇳",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1F4",
      "name": "flag: Somalia",
      "image": "🇸🇴",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1F7",
      "name": "flag: Suriname",
      "image": "🇸🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1F8",
      "name": "flag: South Sudan",
      "image": "🇸🇸",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1F9",
      "name": "flag: São Tomé & Príncipe",
      "image": "🇸🇹",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1FB",
      "name": "flag: El Salvador",
      "image": "🇸🇻",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1FD",
      "name": "flag: Sint Maarten",
      "image": "🇸🇽",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1FE",
      "name": "flag: Syria",
      "image": "🇸🇾",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1FF",
      "name": "flag: Eswatini",
      "image": "🇸🇿",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1E6",
      "name": "flag: Tristan da Cunha",
      "image": "🇹🇦",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1E8",
      "name": "flag: Turks & Caicos Islands",
      "image": "🇹🇨",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1E9",
      "name": "flag: Chad",
      "image": "🇹🇩",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1EB",
      "name": "flag: French Southern Territories",
      "image": "🇹🇫",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1EC",
      "name": "flag: Togo",
      "image": "🇹🇬",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1ED",
      "name": "flag: Thailand",
      "image": "🇹🇭",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1EF",
      "name": "flag: Tajikistan",
      "image": "🇹🇯",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1F0",
      "name": "flag: Tokelau",
      "image": "🇹🇰",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1F1",
      "name": "flag: Timor-Leste",
      "image": "🇹🇱",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1F2",
      "name": "flag: Turkmenistan",
      "image": "🇹🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1F3",
      "name": "flag: Tunisia",
      "image": "🇹🇳",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1F4",
      "name": "flag: Tonga",
      "image": "🇹🇴",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1F7",
      "name": "flag: Turkey",
      "image": "🇹🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1F9",
      "name": "flag: Trinidad & Tobago",
      "image": "🇹🇹",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1FB",
      "name": "flag: Tuvalu",
      "image": "🇹🇻",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1FC",
      "name": "flag: Taiwan",
      "image": "🇹🇼",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1FF",
      "name": "flag: Tanzania",
      "image": "🇹🇿",
      "category": "Flags"
    },
    {
      "code": "U+1F1FA U+1F1E6",
      "name": "flag: Ukraine",
      "image": "🇺🇦",
      "category": "Flags"
    },
    {
      "code": "U+1F1FA U+1F1EC",
      "name": "flag: Uganda",
      "image": "🇺🇬",
      "category": "Flags"
    },
    {
      "code": "U+1F1FA U+1F1F2",
      "name": "flag: U.S. Outlying Islands",
      "image": "🇺🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1FA U+1F1F3",
      "name": "flag: United Nations",
      "image": "🇺🇳",
      "category": "Flags"
    },
    {
      "code": "U+1F1FA U+1F1F8",
      "name": "flag: United States",
      "image": "🇺🇸",
      "category": "Flags"
    },
    {
      "code": "U+1F1FA U+1F1FE",
      "name": "flag: Uruguay",
      "image": "🇺🇾",
      "category": "Flags"
    },
    {
      "code": "U+1F1FA U+1F1FF",
      "name": "flag: Uzbekistan",
      "image": "🇺🇿",
      "category": "Flags"
    },
    {
      "code": "U+1F1FB U+1F1E6",
      "name": "flag: Vatican City",
      "image": "🇻🇦",
      "category": "Flags"
    },
    {
      "code": "U+1F1FB U+1F1E8",
      "name": "flag: St. Vincent & Grenadines",
      "image": "🇻🇨",
      "category": "Flags"
    },
    {
      "code": "U+1F1FB U+1F1EA",
      "name": "flag: Venezuela",
      "image": "🇻🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1FB U+1F1EC",
      "name": "flag: British Virgin Islands",
      "image": "🇻🇬",
      "category": "Flags"
    },
    {
      "code": "U+1F1FB U+1F1EE",
      "name": "flag: U.S. Virgin Islands",
      "image": "🇻🇮",
      "category": "Flags"
    },
    {
      "code": "U+1F1FB U+1F1F3",
      "name": "flag: Vietnam",
      "image": "🇻🇳",
      "category": "Flags"
    },
    {
      "code": "U+1F1FB U+1F1FA",
      "name": "flag: Vanuatu",
      "image": "🇻🇺",
      "category": "Flags"
    },
    {
      "code": "U+1F1FC U+1F1EB",
      "name": "flag: Wallis & Futuna",
      "image": "🇼🇫",
      "category": "Flags"
    },
    {
      "code": "U+1F1FC U+1F1F8",
      "name": "flag: Samoa",
      "image": "🇼🇸",
      "category": "Flags"
    },
    {
      "code": "U+1F1FD U+1F1F0",
      "name": "flag: Kosovo",
      "image": "🇽🇰",
      "category": "Flags"
    },
    {
      "code": "U+1F1FE U+1F1EA",
      "name": "flag: Yemen",
      "image": "🇾🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1FE U+1F1F9",
      "name": "flag: Mayotte",
      "image": "🇾🇹",
      "category": "Flags"
    },
    {
      "code": "U+1F1FF U+1F1E6",
      "name": "flag: South Africa",
      "image": "🇿🇦",
      "category": "Flags"
    },
    {
      "code": "U+1F1FF U+1F1F2",
      "name": "flag: Zambia",
      "image": "🇿🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1FF U+1F1FC",
      "name": "flag: Zimbabwe",
      "image": "🇿🇼",
      "category": "Flags"
    },
    {
      "code": "U+1F3F4 U+E0067 U+E0062 U+E0065 U+E006E U+E0067 U+E007F",
      "name": "flag: England",
      "image": "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
      "category": "Flags"
    },
    {
      "code": "U+1F3F4 U+E0067 U+E0062 U+E0073 U+E0063 U+E0074 U+E007F",
      "name": "flag: Scotland",
      "image": "🏴󠁧󠁢󠁳󠁣󠁴󠁿",
      "category": "Flags"
    },
    {
      "code": "U+1F3F4 U+E0067 U+E0062 U+E0077 U+E006C U+E0073 U+E007F",
      "name": "flag: Wales",
      "image": "🏴󠁧󠁢󠁷󠁬󠁳󠁿",
      "category": "Flags"
    },
    {
      "code": "U+1F3C1",
      "name": "chequered flag",
      "image": "🏁",
      "category": "Flags"
    },
    {
      "code": "U+1F6A9",
      "name": "triangular flag",
      "image": "🚩",
      "category": "Flags"
    },
    {
      "code": "U+1F38C",
      "name": "crossed flags",
      "image": "🎌",
      "category": "Flags"
    },
    {
      "code": "U+1F3F4",
      "name": "black flag",
      "image": "🏴",
      "category": "Flags"
    },
    {
      "code": "U+1F3F3",
      "name": "white flag",
      "image": "🏳",
      "category": "Flags"
    },
    {
      "code": "U+1F3F3 U+FE0F U+200D U+1F308",
      "name": "rainbow flag",
      "image": "🏳️‍🌈",
      "category": "Flags"
    },
    {
      "code": "U+1F3F3 U+FE0F U+200D U+26A7 U+FE0F",
      "name": "transgender flag",
      "image": "🏳️‍⚧️",
      "category": "Flags"
    },
    {
      "code": "U+1F3F4 U+200D U+2620 U+FE0F",
      "name": "pirate flag",
      "image": "🏴‍☠️",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1E8",
      "name": "flag: Ascension Island",
      "image": "🇦🇨",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1E9",
      "name": "flag: Andorra",
      "image": "🇦🇩",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1EA",
      "name": "flag: United Arab Emirates",
      "image": "🇦🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1EB",
      "name": "flag: Afghanistan",
      "image": "🇦🇫",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1EC",
      "name": "flag: Antigua & Barbuda",
      "image": "🇦🇬",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1EE",
      "name": "flag: Anguilla",
      "image": "🇦🇮",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1F1",
      "name": "flag: Albania",
      "image": "🇦🇱",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1F2",
      "name": "flag: Armenia",
      "image": "🇦🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1F4",
      "name": "flag: Angola",
      "image": "🇦🇴",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1F6",
      "name": "flag: Antarctica",
      "image": "🇦🇶",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1F7",
      "name": "flag: Argentina",
      "image": "🇦🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1F8",
      "name": "flag: American Samoa",
      "image": "🇦🇸",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1F9",
      "name": "flag: Austria",
      "image": "🇦🇹",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1FA",
      "name": "flag: Australia",
      "image": "🇦🇺",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1FC",
      "name": "flag: Aruba",
      "image": "🇦🇼",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1FD",
      "name": "flag: Åland Islands",
      "image": "🇦🇽",
      "category": "Flags"
    },
    {
      "code": "U+1F1E6 U+1F1FF",
      "name": "flag: Azerbaijan",
      "image": "🇦🇿",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1E6",
      "name": "flag: Bosnia & Herzegovina",
      "image": "🇧🇦",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1E7",
      "name": "flag: Barbados",
      "image": "🇧🇧",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1E9",
      "name": "flag: Bangladesh",
      "image": "🇧🇩",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1EA",
      "name": "flag: Belgium",
      "image": "🇧🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1EB",
      "name": "flag: Burkina Faso",
      "image": "🇧🇫",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1EC",
      "name": "flag: Bulgaria",
      "image": "🇧🇬",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1ED",
      "name": "flag: Bahrain",
      "image": "🇧🇭",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1EE",
      "name": "flag: Burundi",
      "image": "🇧🇮",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1EF",
      "name": "flag: Benin",
      "image": "🇧🇯",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1F1",
      "name": "flag: St. Barthélemy",
      "image": "🇧🇱",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1F2",
      "name": "flag: Bermuda",
      "image": "🇧🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1F3",
      "name": "flag: Brunei",
      "image": "🇧🇳",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1F4",
      "name": "flag: Bolivia",
      "image": "🇧🇴",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1F6",
      "name": "flag: Caribbean Netherlands",
      "image": "🇧🇶",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1F7",
      "name": "flag: Brazil",
      "image": "🇧🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1F8",
      "name": "flag: Bahamas",
      "image": "🇧🇸",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1F9",
      "name": "flag: Bhutan",
      "image": "🇧🇹",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1FB",
      "name": "flag: Bouvet Island",
      "image": "🇧🇻",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1FC",
      "name": "flag: Botswana",
      "image": "🇧🇼",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1FE",
      "name": "flag: Belarus",
      "image": "🇧🇾",
      "category": "Flags"
    },
    {
      "code": "U+1F1E7 U+1F1FF",
      "name": "flag: Belize",
      "image": "🇧🇿",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1E6",
      "name": "flag: Canada",
      "image": "🇨🇦",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1E8",
      "name": "flag: Cocos (Keeling) Islands",
      "image": "🇨🇨",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1E9",
      "name": "flag: Congo - Kinshasa",
      "image": "🇨🇩",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1EB",
      "name": "flag: Central African Republic",
      "image": "🇨🇫",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1EC",
      "name": "flag: Congo - Brazzaville",
      "image": "🇨🇬",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1ED",
      "name": "flag: Switzerland",
      "image": "🇨🇭",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1EE",
      "name": "flag: Côte d’Ivoire",
      "image": "🇨🇮",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1F0",
      "name": "flag: Cook Islands",
      "image": "🇨🇰",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1F1",
      "name": "flag: Chile",
      "image": "🇨🇱",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1F2",
      "name": "flag: Cameroon",
      "image": "🇨🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1F3",
      "name": "flag: China",
      "image": "🇨🇳",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1F4",
      "name": "flag: Colombia",
      "image": "🇨🇴",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1F5",
      "name": "flag: Clipperton Island",
      "image": "🇨🇵",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1F7",
      "name": "flag: Costa Rica",
      "image": "🇨🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1FA",
      "name": "flag: Cuba",
      "image": "🇨🇺",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1FB",
      "name": "flag: Cape Verde",
      "image": "🇨🇻",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1FC",
      "name": "flag: Curaçao",
      "image": "🇨🇼",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1FD",
      "name": "flag: Christmas Island",
      "image": "🇨🇽",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1FE",
      "name": "flag: Cyprus",
      "image": "🇨🇾",
      "category": "Flags"
    },
    {
      "code": "U+1F1E8 U+1F1FF",
      "name": "flag: Czechia",
      "image": "🇨🇿",
      "category": "Flags"
    },
    {
      "code": "U+1F1E9 U+1F1EA",
      "name": "flag: Germany",
      "image": "🇩🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1E9 U+1F1EC",
      "name": "flag: Diego Garcia",
      "image": "🇩🇬",
      "category": "Flags"
    },
    {
      "code": "U+1F1E9 U+1F1EF",
      "name": "flag: Djibouti",
      "image": "🇩🇯",
      "category": "Flags"
    },
    {
      "code": "U+1F1E9 U+1F1F0",
      "name": "flag: Denmark",
      "image": "🇩🇰",
      "category": "Flags"
    },
    {
      "code": "U+1F1E9 U+1F1F2",
      "name": "flag: Dominica",
      "image": "🇩🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1E9 U+1F1F4",
      "name": "flag: Dominican Republic",
      "image": "🇩🇴",
      "category": "Flags"
    },
    {
      "code": "U+1F1E9 U+1F1FF",
      "name": "flag: Algeria",
      "image": "🇩🇿",
      "category": "Flags"
    },
    {
      "code": "U+1F1EA U+1F1E6",
      "name": "flag: Ceuta & Melilla",
      "image": "🇪🇦",
      "category": "Flags"
    },
    {
      "code": "U+1F1EA U+1F1E8",
      "name": "flag: Ecuador",
      "image": "🇪🇨",
      "category": "Flags"
    },
    {
      "code": "U+1F1EA U+1F1EA",
      "name": "flag: Estonia",
      "image": "🇪🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1EA U+1F1EC",
      "name": "flag: Egypt",
      "image": "🇪🇬",
      "category": "Flags"
    },
    {
      "code": "U+1F1EA U+1F1ED",
      "name": "flag: Western Sahara",
      "image": "🇪🇭",
      "category": "Flags"
    },
    {
      "code": "U+1F1EA U+1F1F7",
      "name": "flag: Eritrea",
      "image": "🇪🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1EA U+1F1F8",
      "name": "flag: Spain",
      "image": "🇪🇸",
      "category": "Flags"
    },
    {
      "code": "U+1F1EA U+1F1F9",
      "name": "flag: Ethiopia",
      "image": "🇪🇹",
      "category": "Flags"
    },
    {
      "code": "U+1F1EA U+1F1FA",
      "name": "flag: European Union",
      "image": "🇪🇺",
      "category": "Flags"
    },
    {
      "code": "U+1F1EB U+1F1EE",
      "name": "flag: Finland",
      "image": "🇫🇮",
      "category": "Flags"
    },
    {
      "code": "U+1F1EB U+1F1EF",
      "name": "flag: Fiji",
      "image": "🇫🇯",
      "category": "Flags"
    },
    {
      "code": "U+1F1EB U+1F1F0",
      "name": "flag: Falkland Islands",
      "image": "🇫🇰",
      "category": "Flags"
    },
    {
      "code": "U+1F1EB U+1F1F2",
      "name": "flag: Micronesia",
      "image": "🇫🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1EB U+1F1F4",
      "name": "flag: Faroe Islands",
      "image": "🇫🇴",
      "category": "Flags"
    },
    {
      "code": "U+1F1EB U+1F1F7",
      "name": "flag: France",
      "image": "🇫🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1E6",
      "name": "flag: Gabon",
      "image": "🇬🇦",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1E7",
      "name": "flag: United Kingdom",
      "image": "🇬🇧",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1E9",
      "name": "flag: Grenada",
      "image": "🇬🇩",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1EA",
      "name": "flag: Georgia",
      "image": "🇬🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1EB",
      "name": "flag: French Guiana",
      "image": "🇬🇫",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1EC",
      "name": "flag: Guernsey",
      "image": "🇬🇬",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1ED",
      "name": "flag: Ghana",
      "image": "🇬🇭",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1EE",
      "name": "flag: Gibraltar",
      "image": "🇬🇮",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1F1",
      "name": "flag: Greenland",
      "image": "🇬🇱",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1F2",
      "name": "flag: Gambia",
      "image": "🇬🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1F3",
      "name": "flag: Guinea",
      "image": "🇬🇳",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1F5",
      "name": "flag: Guadeloupe",
      "image": "🇬🇵",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1F6",
      "name": "flag: Equatorial Guinea",
      "image": "🇬🇶",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1F7",
      "name": "flag: Greece",
      "image": "🇬🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1F8",
      "name": "flag: South Georgia & South Sandwich Islands",
      "image": "🇬🇸",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1F9",
      "name": "flag: Guatemala",
      "image": "🇬🇹",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1FA",
      "name": "flag: Guam",
      "image": "🇬🇺",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1FC",
      "name": "flag: Guinea-Bissau",
      "image": "🇬🇼",
      "category": "Flags"
    },
    {
      "code": "U+1F1EC U+1F1FE",
      "name": "flag: Guyana",
      "image": "🇬🇾",
      "category": "Flags"
    },
    {
      "code": "U+1F1ED U+1F1F0",
      "name": "flag: Hong Kong SAR China",
      "image": "🇭🇰",
      "category": "Flags"
    },
    {
      "code": "U+1F1ED U+1F1F2",
      "name": "flag: Heard & McDonald Islands",
      "image": "🇭🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1ED U+1F1F3",
      "name": "flag: Honduras",
      "image": "🇭🇳",
      "category": "Flags"
    },
    {
      "code": "U+1F1ED U+1F1F7",
      "name": "flag: Croatia",
      "image": "🇭🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1ED U+1F1F9",
      "name": "flag: Haiti",
      "image": "🇭🇹",
      "category": "Flags"
    },
    {
      "code": "U+1F1ED U+1F1FA",
      "name": "flag: Hungary",
      "image": "🇭🇺",
      "category": "Flags"
    },
    {
      "code": "U+1F1EE U+1F1E8",
      "name": "flag: Canary Islands",
      "image": "🇮🇨",
      "category": "Flags"
    },
    {
      "code": "U+1F1EE U+1F1E9",
      "name": "flag: Indonesia",
      "image": "🇮🇩",
      "category": "Flags"
    },
    {
      "code": "U+1F1EE U+1F1EA",
      "name": "flag: Ireland",
      "image": "🇮🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1EE U+1F1F1",
      "name": "flag: Israel",
      "image": "🇮🇱",
      "category": "Flags"
    },
    {
      "code": "U+1F1EE U+1F1F2",
      "name": "flag: Isle of Man",
      "image": "🇮🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1EE U+1F1F3",
      "name": "flag: India",
      "image": "🇮🇳",
      "category": "Flags"
    },
    {
      "code": "U+1F1EE U+1F1F4",
      "name": "flag: British Indian Ocean Territory",
      "image": "🇮🇴",
      "category": "Flags"
    },
    {
      "code": "U+1F1EE U+1F1F6",
      "name": "flag: Iraq",
      "image": "🇮🇶",
      "category": "Flags"
    },
    {
      "code": "U+1F1EE U+1F1F7",
      "name": "flag: Iran",
      "image": "🇮🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1EE U+1F1F8",
      "name": "flag: Iceland",
      "image": "🇮🇸",
      "category": "Flags"
    },
    {
      "code": "U+1F1EE U+1F1F9",
      "name": "flag: Italy",
      "image": "🇮🇹",
      "category": "Flags"
    },
    {
      "code": "U+1F1EF U+1F1EA",
      "name": "flag: Jersey",
      "image": "🇯🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1EF U+1F1F2",
      "name": "flag: Jamaica",
      "image": "🇯🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1EF U+1F1F4",
      "name": "flag: Jordan",
      "image": "🇯🇴",
      "category": "Flags"
    },
    {
      "code": "U+1F1EF U+1F1F5",
      "name": "flag: Japan",
      "image": "🇯🇵",
      "category": "Flags"
    },
    {
      "code": "U+1F1F0 U+1F1EA",
      "name": "flag: Kenya",
      "image": "🇰🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1F0 U+1F1EC",
      "name": "flag: Kyrgyzstan",
      "image": "🇰🇬",
      "category": "Flags"
    },
    {
      "code": "U+1F1F0 U+1F1ED",
      "name": "flag: Cambodia",
      "image": "🇰🇭",
      "category": "Flags"
    },
    {
      "code": "U+1F1F0 U+1F1EE",
      "name": "flag: Kiribati",
      "image": "🇰🇮",
      "category": "Flags"
    },
    {
      "code": "U+1F1F0 U+1F1F2",
      "name": "flag: Comoros",
      "image": "🇰🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1F0 U+1F1F3",
      "name": "flag: St. Kitts & Nevis",
      "image": "🇰🇳",
      "category": "Flags"
    },
    {
      "code": "U+1F1F0 U+1F1F5",
      "name": "flag: North Korea",
      "image": "🇰🇵",
      "category": "Flags"
    },
    {
      "code": "U+1F1F0 U+1F1F7",
      "name": "flag: South Korea",
      "image": "🇰🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1F0 U+1F1FC",
      "name": "flag: Kuwait",
      "image": "🇰🇼",
      "category": "Flags"
    },
    {
      "code": "U+1F1F0 U+1F1FE",
      "name": "flag: Cayman Islands",
      "image": "🇰🇾",
      "category": "Flags"
    },
    {
      "code": "U+1F1F0 U+1F1FF",
      "name": "flag: Kazakhstan",
      "image": "🇰🇿",
      "category": "Flags"
    },
    {
      "code": "U+1F1F1 U+1F1E6",
      "name": "flag: Laos",
      "image": "🇱🇦",
      "category": "Flags"
    },
    {
      "code": "U+1F1F1 U+1F1E7",
      "name": "flag: Lebanon",
      "image": "🇱🇧",
      "category": "Flags"
    },
    {
      "code": "U+1F1F1 U+1F1E8",
      "name": "flag: St. Lucia",
      "image": "🇱🇨",
      "category": "Flags"
    },
    {
      "code": "U+1F1F1 U+1F1EE",
      "name": "flag: Liechtenstein",
      "image": "🇱🇮",
      "category": "Flags"
    },
    {
      "code": "U+1F1F1 U+1F1F0",
      "name": "flag: Sri Lanka",
      "image": "🇱🇰",
      "category": "Flags"
    },
    {
      "code": "U+1F1F1 U+1F1F7",
      "name": "flag: Liberia",
      "image": "🇱🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1F1 U+1F1F8",
      "name": "flag: Lesotho",
      "image": "🇱🇸",
      "category": "Flags"
    },
    {
      "code": "U+1F1F1 U+1F1F9",
      "name": "flag: Lithuania",
      "image": "🇱🇹",
      "category": "Flags"
    },
    {
      "code": "U+1F1F1 U+1F1FA",
      "name": "flag: Luxembourg",
      "image": "🇱🇺",
      "category": "Flags"
    },
    {
      "code": "U+1F1F1 U+1F1FB",
      "name": "flag: Latvia",
      "image": "🇱🇻",
      "category": "Flags"
    },
    {
      "code": "U+1F1F1 U+1F1FE",
      "name": "flag: Libya",
      "image": "🇱🇾",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1E6",
      "name": "flag: Morocco",
      "image": "🇲🇦",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1E8",
      "name": "flag: Monaco",
      "image": "🇲🇨",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1E9",
      "name": "flag: Moldova",
      "image": "🇲🇩",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1EA",
      "name": "flag: Montenegro",
      "image": "🇲🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1EB",
      "name": "flag: St. Martin",
      "image": "🇲🇫",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1EC",
      "name": "flag: Madagascar",
      "image": "🇲🇬",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1ED",
      "name": "flag: Marshall Islands",
      "image": "🇲🇭",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1F0",
      "name": "flag: North Macedonia",
      "image": "🇲🇰",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1F1",
      "name": "flag: Mali",
      "image": "🇲🇱",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1F2",
      "name": "flag: Myanmar (Burma)",
      "image": "🇲🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1F3",
      "name": "flag: Mongolia",
      "image": "🇲🇳",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1F4",
      "name": "flag: Macao SAR China",
      "image": "🇲🇴",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1F5",
      "name": "flag: Northern Mariana Islands",
      "image": "🇲🇵",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1F6",
      "name": "flag: Martinique",
      "image": "🇲🇶",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1F7",
      "name": "flag: Mauritania",
      "image": "🇲🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1F8",
      "name": "flag: Montserrat",
      "image": "🇲🇸",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1F9",
      "name": "flag: Malta",
      "image": "🇲🇹",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1FA",
      "name": "flag: Mauritius",
      "image": "🇲🇺",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1FB",
      "name": "flag: Maldives",
      "image": "🇲🇻",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1FC",
      "name": "flag: Malawi",
      "image": "🇲🇼",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1FD",
      "name": "flag: Mexico",
      "image": "🇲🇽",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1FE",
      "name": "flag: Malaysia",
      "image": "🇲🇾",
      "category": "Flags"
    },
    {
      "code": "U+1F1F2 U+1F1FF",
      "name": "flag: Mozambique",
      "image": "🇲🇿",
      "category": "Flags"
    },
    {
      "code": "U+1F1F3 U+1F1E6",
      "name": "flag: Namibia",
      "image": "🇳🇦",
      "category": "Flags"
    },
    {
      "code": "U+1F1F3 U+1F1E8",
      "name": "flag: New Caledonia",
      "image": "🇳🇨",
      "category": "Flags"
    },
    {
      "code": "U+1F1F3 U+1F1EA",
      "name": "flag: Niger",
      "image": "🇳🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1F3 U+1F1EB",
      "name": "flag: Norfolk Island",
      "image": "🇳🇫",
      "category": "Flags"
    },
    {
      "code": "U+1F1F3 U+1F1EC",
      "name": "flag: Nigeria",
      "image": "🇳🇬",
      "category": "Flags"
    },
    {
      "code": "U+1F1F3 U+1F1EE",
      "name": "flag: Nicaragua",
      "image": "🇳🇮",
      "category": "Flags"
    },
    {
      "code": "U+1F1F3 U+1F1F1",
      "name": "flag: Netherlands",
      "image": "🇳🇱",
      "category": "Flags"
    },
    {
      "code": "U+1F1F3 U+1F1F4",
      "name": "flag: Norway",
      "image": "🇳🇴",
      "category": "Flags"
    },
    {
      "code": "U+1F1F3 U+1F1F5",
      "name": "flag: Nepal",
      "image": "🇳🇵",
      "category": "Flags"
    },
    {
      "code": "U+1F1F3 U+1F1F7",
      "name": "flag: Nauru",
      "image": "🇳🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1F3 U+1F1FA",
      "name": "flag: Niue",
      "image": "🇳🇺",
      "category": "Flags"
    },
    {
      "code": "U+1F1F3 U+1F1FF",
      "name": "flag: New Zealand",
      "image": "🇳🇿",
      "category": "Flags"
    },
    {
      "code": "U+1F1F4 U+1F1F2",
      "name": "flag: Oman",
      "image": "🇴🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1F5 U+1F1E6",
      "name": "flag: Panama",
      "image": "🇵🇦",
      "category": "Flags"
    },
    {
      "code": "U+1F1F5 U+1F1EA",
      "name": "flag: Peru",
      "image": "🇵🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1F5 U+1F1EB",
      "name": "flag: French Polynesia",
      "image": "🇵🇫",
      "category": "Flags"
    },
    {
      "code": "U+1F1F5 U+1F1EC",
      "name": "flag: Papua New Guinea",
      "image": "🇵🇬",
      "category": "Flags"
    },
    {
      "code": "U+1F1F5 U+1F1ED",
      "name": "flag: Philippines",
      "image": "🇵🇭",
      "category": "Flags"
    },
    {
      "code": "U+1F1F5 U+1F1F0",
      "name": "flag: Pakistan",
      "image": "🇵🇰",
      "category": "Flags"
    },
    {
      "code": "U+1F1F5 U+1F1F1",
      "name": "flag: Poland",
      "image": "🇵🇱",
      "category": "Flags"
    },
    {
      "code": "U+1F1F5 U+1F1F2",
      "name": "flag: St. Pierre & Miquelon",
      "image": "🇵🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1F5 U+1F1F3",
      "name": "flag: Pitcairn Islands",
      "image": "🇵🇳",
      "category": "Flags"
    },
    {
      "code": "U+1F1F5 U+1F1F7",
      "name": "flag: Puerto Rico",
      "image": "🇵🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1F5 U+1F1F8",
      "name": "flag: Palestinian Territories",
      "image": "🇵🇸",
      "category": "Flags"
    },
    {
      "code": "U+1F1F5 U+1F1F9",
      "name": "flag: Portugal",
      "image": "🇵🇹",
      "category": "Flags"
    },
    {
      "code": "U+1F1F5 U+1F1FC",
      "name": "flag: Palau",
      "image": "🇵🇼",
      "category": "Flags"
    },
    {
      "code": "U+1F1F5 U+1F1FE",
      "name": "flag: Paraguay",
      "image": "🇵🇾",
      "category": "Flags"
    },
    {
      "code": "U+1F1F6 U+1F1E6",
      "name": "flag: Qatar",
      "image": "🇶🇦",
      "category": "Flags"
    },
    {
      "code": "U+1F1F7 U+1F1EA",
      "name": "flag: Réunion",
      "image": "🇷🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1F7 U+1F1F4",
      "name": "flag: Romania",
      "image": "🇷🇴",
      "category": "Flags"
    },
    {
      "code": "U+1F1F7 U+1F1F8",
      "name": "flag: Serbia",
      "image": "🇷🇸",
      "category": "Flags"
    },
    {
      "code": "U+1F1F7 U+1F1FA",
      "name": "flag: Russia",
      "image": "🇷🇺",
      "category": "Flags"
    },
    {
      "code": "U+1F1F7 U+1F1FC",
      "name": "flag: Rwanda",
      "image": "🇷🇼",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1E6",
      "name": "flag: Saudi Arabia",
      "image": "🇸🇦",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1E7",
      "name": "flag: Solomon Islands",
      "image": "🇸🇧",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1E8",
      "name": "flag: Seychelles",
      "image": "🇸🇨",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1E9",
      "name": "flag: Sudan",
      "image": "🇸🇩",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1EA",
      "name": "flag: Sweden",
      "image": "🇸🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1EC",
      "name": "flag: Singapore",
      "image": "🇸🇬",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1ED",
      "name": "flag: St. Helena",
      "image": "🇸🇭",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1EE",
      "name": "flag: Slovenia",
      "image": "🇸🇮",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1EF",
      "name": "flag: Svalbard & Jan Mayen",
      "image": "🇸🇯",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1F0",
      "name": "flag: Slovakia",
      "image": "🇸🇰",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1F1",
      "name": "flag: Sierra Leone",
      "image": "🇸🇱",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1F2",
      "name": "flag: San Marino",
      "image": "🇸🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1F3",
      "name": "flag: Senegal",
      "image": "🇸🇳",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1F4",
      "name": "flag: Somalia",
      "image": "🇸🇴",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1F7",
      "name": "flag: Suriname",
      "image": "🇸🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1F8",
      "name": "flag: South Sudan",
      "image": "🇸🇸",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1F9",
      "name": "flag: São Tomé & Príncipe",
      "image": "🇸🇹",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1FB",
      "name": "flag: El Salvador",
      "image": "🇸🇻",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1FD",
      "name": "flag: Sint Maarten",
      "image": "🇸🇽",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1FE",
      "name": "flag: Syria",
      "image": "🇸🇾",
      "category": "Flags"
    },
    {
      "code": "U+1F1F8 U+1F1FF",
      "name": "flag: Eswatini",
      "image": "🇸🇿",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1E6",
      "name": "flag: Tristan da Cunha",
      "image": "🇹🇦",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1E8",
      "name": "flag: Turks & Caicos Islands",
      "image": "🇹🇨",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1E9",
      "name": "flag: Chad",
      "image": "🇹🇩",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1EB",
      "name": "flag: French Southern Territories",
      "image": "🇹🇫",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1EC",
      "name": "flag: Togo",
      "image": "🇹🇬",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1ED",
      "name": "flag: Thailand",
      "image": "🇹🇭",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1EF",
      "name": "flag: Tajikistan",
      "image": "🇹🇯",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1F0",
      "name": "flag: Tokelau",
      "image": "🇹🇰",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1F1",
      "name": "flag: Timor-Leste",
      "image": "🇹🇱",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1F2",
      "name": "flag: Turkmenistan",
      "image": "🇹🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1F3",
      "name": "flag: Tunisia",
      "image": "🇹🇳",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1F4",
      "name": "flag: Tonga",
      "image": "🇹🇴",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1F7",
      "name": "flag: Turkey",
      "image": "🇹🇷",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1F9",
      "name": "flag: Trinidad & Tobago",
      "image": "🇹🇹",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1FB",
      "name": "flag: Tuvalu",
      "image": "🇹🇻",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1FC",
      "name": "flag: Taiwan",
      "image": "🇹🇼",
      "category": "Flags"
    },
    {
      "code": "U+1F1F9 U+1F1FF",
      "name": "flag: Tanzania",
      "image": "🇹🇿",
      "category": "Flags"
    },
    {
      "code": "U+1F1FA U+1F1E6",
      "name": "flag: Ukraine",
      "image": "🇺🇦",
      "category": "Flags"
    },
    {
      "code": "U+1F1FA U+1F1EC",
      "name": "flag: Uganda",
      "image": "🇺🇬",
      "category": "Flags"
    },
    {
      "code": "U+1F1FA U+1F1F2",
      "name": "flag: U.S. Outlying Islands",
      "image": "🇺🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1FA U+1F1F3",
      "name": "flag: United Nations",
      "image": "🇺🇳",
      "category": "Flags"
    },
    {
      "code": "U+1F1FA U+1F1F8",
      "name": "flag: United States",
      "image": "🇺🇸",
      "category": "Flags"
    },
    {
      "code": "U+1F1FA U+1F1FE",
      "name": "flag: Uruguay",
      "image": "🇺🇾",
      "category": "Flags"
    },
    {
      "code": "U+1F1FA U+1F1FF",
      "name": "flag: Uzbekistan",
      "image": "🇺🇿",
      "category": "Flags"
    },
    {
      "code": "U+1F1FB U+1F1E6",
      "name": "flag: Vatican City",
      "image": "🇻🇦",
      "category": "Flags"
    },
    {
      "code": "U+1F1FB U+1F1E8",
      "name": "flag: St. Vincent & Grenadines",
      "image": "🇻🇨",
      "category": "Flags"
    },
    {
      "code": "U+1F1FB U+1F1EA",
      "name": "flag: Venezuela",
      "image": "🇻🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1FB U+1F1EC",
      "name": "flag: British Virgin Islands",
      "image": "🇻🇬",
      "category": "Flags"
    },
    {
      "code": "U+1F1FB U+1F1EE",
      "name": "flag: U.S. Virgin Islands",
      "image": "🇻🇮",
      "category": "Flags"
    },
    {
      "code": "U+1F1FB U+1F1F3",
      "name": "flag: Vietnam",
      "image": "🇻🇳",
      "category": "Flags"
    },
    {
      "code": "U+1F1FB U+1F1FA",
      "name": "flag: Vanuatu",
      "image": "🇻🇺",
      "category": "Flags"
    },
    {
      "code": "U+1F1FC U+1F1EB",
      "name": "flag: Wallis & Futuna",
      "image": "🇼🇫",
      "category": "Flags"
    },
    {
      "code": "U+1F1FC U+1F1F8",
      "name": "flag: Samoa",
      "image": "🇼🇸",
      "category": "Flags"
    },
    {
      "code": "U+1F1FD U+1F1F0",
      "name": "flag: Kosovo",
      "image": "🇽🇰",
      "category": "Flags"
    },
    {
      "code": "U+1F1FE U+1F1EA",
      "name": "flag: Yemen",
      "image": "🇾🇪",
      "category": "Flags"
    },
    {
      "code": "U+1F1FE U+1F1F9",
      "name": "flag: Mayotte",
      "image": "🇾🇹",
      "category": "Flags"
    },
    {
      "code": "U+1F1FF U+1F1E6",
      "name": "flag: South Africa",
      "image": "🇿🇦",
      "category": "Flags"
    },
    {
      "code": "U+1F1FF U+1F1F2",
      "name": "flag: Zambia",
      "image": "🇿🇲",
      "category": "Flags"
    },
    {
      "code": "U+1F1FF U+1F1FC",
      "name": "flag: Zimbabwe",
      "image": "🇿🇼",
      "category": "Flags"
    },
    {
      "code": "U+1F3F4 U+E0067 U+E0062 U+E0065 U+E006E U+E0067 U+E007F",
      "name": "flag: England",
      "image": "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
      "category": "Flags"
    },
    {
      "code": "U+1F3F4 U+E0067 U+E0062 U+E0073 U+E0063 U+E0074 U+E007F",
      "name": "flag: Scotland",
      "image": "🏴󠁧󠁢󠁳󠁣󠁴󠁿",
      "category": "Flags"
    },
    {
      "code": "U+1F3F4 U+E0067 U+E0062 U+E0077 U+E006C U+E0073 U+E007F",
      "name": "flag: Wales",
      "image": "🏴󠁧󠁢󠁷󠁬󠁳󠁿",
      "category": "Flags"
    }
  ]


def get_random_emojis(count):
  """
  Returns a list of count number of random smiley objects from the list
  """
  return random.sample(smileys, count)


def get_random_emojis_by_category(category, count):
  """
  Returns a list of count number of smiley objects from the list with the given category
  """
  smileys_filtered = [smiley for smiley in smileys if smiley["category"] == category]
  return random.sample(smileys_filtered, count)