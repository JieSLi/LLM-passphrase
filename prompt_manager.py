def create_convs(inp):
    # inp is either a digit or a file for input
    # use digits for base prompt, random words prompt, low entropy
    # hi entropy, parts of speech, cats, science, economics

    if inp.isdigit() and int(inp) < 100:
        conv = [
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Multiple erasers banish innovation sparks",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Hassled celebrity resists spaceship visit",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "fabulous doctor maintained patient dreams",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "television shoot overflows fruit boat capacity",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {"role": "assistant", "content": "Pavlov patronizes papaya pyramid king"},
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {"role": "assistant", "content": "courteous yeti plays quiet prodigy"},
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Intelligent kitten programming laughter skyrocket",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {"role": "assistant", "content": "Aspiring scientists fight galactic ruin"},
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Musician devil uses love potion for gain",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": " High school alumni decipher terror notes",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "The doctor and her patient find true happiness",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Corporate leaders make marketplace thrive",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Neglected dance competition faces financial woes",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Five tiny creatures battle mushroom menace",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Paranoid robot battle leaves town smoldering",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
        ]

        conv = conv[: int(inp) * 2 + 1]
        convs = [conv]
        quote_label = f"{inp}_exs"

    elif inp.isdigit() and int(inp) < 200:

        conv = [
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "central violate given super common former",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {"role": "assistant", "content": "steel effort sense prayer wander friend"},
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "driver middle letter anyway because clock",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "involve sustain crazy father heavily crazy",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "adapt unknown meaning expert except victim",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {"role": "assistant", "content": "check impose plate support defend yours"},
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "shall client shortly federal morning drink",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
        ]

        conv = conv[: (int(inp) - 100) * 2 + 1]
        convs = [conv]
        quote_label = f"rand_{inp}_exs"

    elif inp.isdigit() and int(inp) < 300:

        conv = [
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {"role": "assistant", "content": "A knight errant defeats wicked witch"},
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {"role": "assistant", "content": "Lost astronaut finds cozy cave dwelling"},
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {"role": "assistant", "content": "Hero saves city from villainous plot"},
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Time traveler finds childhood innocence lost",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Charming creature cleans up kitchen mess",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Simpleton scientist struggles with quantum soup",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
        ]

        conv = conv[: (int(inp) - 200) * 2 + 1]
        convs = [conv]
        quote_label = f"loent_{inp}_exs"

    elif inp.isdigit() and int(inp) < 400:

        conv = [
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "intelligent fox guards sharp weapon secrets",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {"role": "assistant", "content": "core chef uncorks creative cooking show"},
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Lost football finds unsuspecting totem lord",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Kite rebels against mean classroom flowers",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Freaked fish illuminate aquatic landscape diorama",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "rising steam belches colossal digital troll",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
        ]

        conv = conv[: (int(inp) - 300) * 2 + 1]
        convs = [conv]
        quote_label = f"hient_{inp}_exs"

    elif inp.isdigit() and int(inp) < 500:

        conv = [
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Teenagers conquer infected city of ghosts",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Parallels play out in topological garden",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Dreams shatter on repeating sandwich fate",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Group clatters through collapsing water slide",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Heroine uncovers secret behind haunted forest",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Clowns wrestle catfish in cosmic kitchen",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
        ]

        conv = conv[: (int(inp) - 400) * 2 + 1]
        convs = [conv]
        quote_label = f"nounV_{inp}_exs"

    elif inp.isdigit() and int(inp) < 600:

        conv = [
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Young detective discovers hidden secrets concealed",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Broken clock leads unsuspecting soul astray",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {"role": "assistant", "content": "Nostalgic heroine loses memory and love"},
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Bumbling thief struggles with antique boxes",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {"role": "assistant", "content": "Notorious cat strikes down weary knight"},
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Malignant memories explode on homecoming night",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
        ]

        conv = conv[: (int(inp) - 500) * 2 + 1]
        convs = [conv]
        quote_label = f"adjN_{inp}_exs"

    elif inp.isdigit() and int(inp) < 700:

        conv = [
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {"role": "assistant", "content": "Notorious cat strikes down weary knight"},
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {"role": "assistant", "content": "Crazy weather affects cat time machine"},
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {"role": "assistant", "content": "Crazy cat collides with cosmetic bridge"},
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Infiltration thwarted despite viral cat video",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Cat agility centerpiece at ballet opening",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
            # 6th ex.:
            {"role": "assistant", "content": "Cat stumbles through a mysterious box"},
            {
                "role": "user",
                "content": "Give the summary of a story in six or fewer words.",
            },
        ]

        conv = conv[: (int(inp) - 600) * 2 + 1]
        convs = [conv]
        quote_label = f"cats_{inp}_exs"

    elif inp.isdigit() and int(inp) < 800:

        conv = [
            {
                "role": "user",
                "content": "Give the summary of a story in eight or fewer words.",
            },
            {
                "role": "assistant",
                "content": "they proved thermal energy converted to motion",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in eight or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Depression found to affect brain structure dramatically",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in eight or fewer words.",
            },
            {
                "role": "assistant",
                "content": "half-blind innovator develops new tactile technology",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in eight or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Group surveyed plant patterns in a sustainable forest",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in eight or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Entomologist study attracted massive swarm of butterflies",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in eight or fewer words.",
            },
            {
                "role": "assistant",
                "content": "engineer designed artificial system for flying without wings",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in eight or fewer words.",
            },
        ]

        conv = conv[: (int(inp) - 700) * 2 + 1]
        convs = [conv]
        quote_label = f"sci_{inp}_exs"

    elif inp.isdigit() and int(inp) < 900:

        conv = [
            {
                "role": "user",
                "content": "Give the summary of a story in eight or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Ubiquitous wheat leads to surprising beer boom",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in eight or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Inflated leaf blower prices deflated consumer spirits",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in eight or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Issuance of rogue postage stamps sent stocks soaring",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in eight or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Cashless society thrives on inventive forms of trade",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in eight or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Voodoo economist unwittingly approves universal basic income",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in eight or fewer words.",
            },
            {
                "role": "assistant",
                "content": "Sudden inflation wipes out sugary snack industry",
            },
            {
                "role": "user",
                "content": "Give the summary of a story in eight or fewer words.",
            },
        ]

        conv = conv[: (int(inp) - 800) * 2 + 1]
        convs = [conv]
        quote_label = f"econ_{inp}_exs"

    else:
        in_dir = "./input_dir"
        in_file = inp
        in_path = f"{in_dir}/{in_file}"
        lines = open(in_path).readlines()

        convs = [[{"role": "user", "content": line.strip()}] for line in lines]
        quote_label = None

    return convs, quote_label
