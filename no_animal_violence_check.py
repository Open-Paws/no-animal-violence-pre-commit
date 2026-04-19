# AUTO-GENERATED from Open-Paws/no-animal-violence. Do not edit directly.
"""Pre-commit hook for detecting language that normalizes violence toward animals."""

import re
import sys


PATTERNS = [
    {"regex": r"kill\s+two\s+birds\s+with\s+one\s+stone", "alternative": "accomplish two things at once", "reason": "This phrase frames killing animals as a routine way to solve a problem. Plain alternatives like 'accomplish two things at once' carry the same meaning without invoking harm."},
    {"regex": r"beat(ing)?\s+a\s+dead\s+horse", "alternative": "belabor the point", "reason": "This phrase uses an image of striking an animal's body as a metaphor for wasted effort. 'Belabor the point' is clearer and skips the imagery."},
    {"regex": r"(more\s+than\s+one|another|different|several)\s+way[s]?\s+to\s+skin\s+a\s+cat", "alternative": "more than one way to peel an orange", "reason": "Cat skinning as a metaphor for having options. 'Multiple approaches available' or 'more than one way to peel an orange' carries the same meaning."},
    {"regex": r"let\s+the\s+cat\s+out\s+of\s+the\s+bag", "alternative": "reveal the secret", "reason": "Traced to fraudulent livestock markets and implies trapping animals. 'Reveal the secret' says the same thing more directly."},
    {"regex": r"open(ing)?\s+a\s+can\s+of\s+worms", "alternative": "create a complicated situation", "reason": "References worms packaged as live bait to catch and kill fish. 'Open a difficult topic' or 'uncover hidden problems' is more precise."},
    {"regex": r"wild\s+goose\s+chase", "alternative": "futile search", "reason": "Casts pursuing a living bird as a pointless annoyance. 'Futile search' or 'fool's errand' says the same thing without the hunting framing."},
    {"regex": r"(like\s+)?shoot(ing)?\s+fish\s+in\s+a\s+barrel", "alternative": "trivially easy", "reason": "Mass-killing imagery used to mean 'easy.' 'Trivially easy' or 'a sure thing' says the same thing without it."},
    {"regex": r"flog(ging)?\s+a\s+dead\s+horse", "alternative": "belabor the point", "reason": "Describes whipping an animal's corpse — the same image as 'beat a dead horse'. 'Belabor the point' is a direct replacement."},
    {"regex": r"(bigger|other)\s+fish\s+to\s+fry", "alternative": "more important matters to address", "reason": "Fish-as-food commodification for 'more important things.' 'More important matters' says the same thing."},
    {"regex": r"\b(?:guinea\s+pig)\b", "alternative": "test subject", "reason": "Refers to using guinea pigs as expendable test subjects in harmful experiments. 'Test subject' or 'early adopter' is more precise in technical contexts."},
    {"regex": r"(?:bring(?:ing|s)?|brought)\s+home\s+the\s+bacon", "alternative": "bring home the results", "reason": "Describes slaughtered pig flesh as the fruit of success. 'Bring home the results' or 'earn a living' carries the same meaning."},
    {"regex": r"tak(e|ing|es|en)\s+the\s+bull\s+by\s+the\s+horns|took\s+the\s+bull\s+by\s+the\s+horns", "alternative": "tackle the problem directly", "reason": "Bullfighting/rodeo imagery. 'Tackle the problem directly' or 'face it head-on' is cleaner."},
    {"regex": r"(like\s+(a\s+)?)?lambs?\s+to\s+the\s+slaughter", "alternative": "without resistance", "reason": "Direct slaughter imagery. 'Without resistance' or 'unknowingly walking into danger' captures the same meaning."},
    {"regex": r"(no|not\s+enough)\s+room\s+to\s+swing\s+a\s+cat", "alternative": "extremely tight space", "reason": "Violent animal imagery for 'cramped.' 'Extremely tight space' says it directly."},
    {"regex": r"\b(?:red\s+herring)\b", "alternative": "distraction", "reason": "Originates from dead, smoked fish reportedly used to train hunting dogs. 'Distraction' or 'false lead' communicates the idea directly."},
    {"regex": r"curiosity\s+killed\s+the\s+cat", "alternative": "curiosity backfired", "reason": "A direct reference to killing a cat, used as a cautionary phrase. 'Curiosity backfired' or 'being nosy caused trouble' says the same thing."},
    {"regex": r"(running\s+around\s+)?like\s+a\s+chicken\s+with\s+(its|their)\s+head\s+cut\s+off", "alternative": "like your hair is on fire", "reason": "Graphic slaughter imagery used to describe panic. 'In a panic' or 'like your hair is on fire' captures the same thing."},
    {"regex": r"(your|their|his|her|my|our)\s+goose\s+is\s+cooked", "alternative": "you're in trouble", "reason": "Killing-and-cooking imagery used to mean someone is in trouble. 'You're in trouble' says it directly."},
    {"regex": r"thr(ow|owing|own|ew)(\s+(someone|them|him|her|us|me))?\s+to\s+the\s+wolves", "alternative": "abandon to criticism", "reason": "Frames a person as prey. 'Abandon to criticism' or 'leave exposed' carries the same meaning without the imagery."},
    {"regex": r"hook,?\s+line,?\s+and\s+sinker", "alternative": "completely", "reason": "References the equipment used to hook and kill fish. 'Completely' or 'without question' conveys total buy-in without the fishing imagery."},
    {"regex": r"clip(s|ped|ping)?\s+(someone's|their|his|her)?\s*wings", "alternative": "restrict freedom", "reason": "Wing-clipping is a real physical mutilation done to captive birds. 'Restrict freedom' or 'limit options' says the same thing directly."},
    {"regex": r"straw\s+that\s+broke\s+the\s+camel'?s\s+back|last\s+straw", "alternative": "tipping point", "reason": "Overloading a pack animal until its back breaks. 'Tipping point' or 'breaking point' carries the same meaning."},
    {"regex": r"(a\s+)?bird\s+in\s+the\s+hand(\s+is\s+worth)?", "alternative": "a sure thing beats a possibility", "reason": "References trapping wild birds. 'A sure thing beats a possibility' carries the same meaning."},
    {"regex": r"\b(?:eat(ing)?\s+crow)\b", "alternative": "admit being wrong", "reason": "References eating a killed bird as humiliating punishment. 'Admit being wrong' or 'swallow one's pride' says the same thing directly."},
    {"regex": r"f(ight|ights|ighting|ought)\s+like\s+cats\s+and\s+dogs", "alternative": "constantly argue", "reason": "Animal-fighting imagery. 'Constantly argue' or 'clash frequently' says it directly."},
    {"regex": r"(?:take|taking|took)\s+the\s+bait", "alternative": "fall for it", "reason": "References baiting hooks and traps to catch and kill animals. 'Fall for it' or 'be deceived' is more direct."},
    {"regex": r"(don'?t\s+)?count(ing)?\s+your\s+chickens(\s+before)?", "alternative": "don't assume success prematurely", "reason": "Commodity framing of chickens as a yield to be counted. 'Don't assume success prematurely' says it directly."},
    {"regex": r"\b(?:livestock)\b", "alternative": "farmed animals", "reason": "Commodity framing that groups sentient beings as 'stock.' 'Farmed animals' keeps the meaning without the commodity framing."},
    {"regex": r"\b(?:poultry)\b", "alternative": "farmed birds", "reason": "Commodity framing for farmed birds. 'Farmed birds' or the specific species keeps the meaning without the commodity framing."},
    {"regex": r"gestation\s+(crate|stall)s?", "alternative": "pregnancy cage", "reason": "Industry euphemism for a metal enclosure so small a pregnant sow cannot turn around for her entire 3.5-month pregnancy. 'Pregnancy cage' is accurate."},
    {"regex": r"\b(?:depopulat(ion|ed|ing))\b", "alternative": "mass killing", "reason": "Industry euphemism for killing entire flocks or herds at once. 'Mass killing' is the accurate term. (Suppressed in database or population-statistics contexts where the word refers to removing records.)"},
    {"regex": r"(meat[\s-]?packing|meat|packing|processing)\s+(plant|facility)s?", "alternative": "slaughterhouse", "reason": "Industry euphemisms for slaughterhouse. 'Slaughterhouse' is the accurate term. (Suppressed in clearly non-animal contexts like data or chemical processing.)"},
    {"regex": r"farrowing\s+(crate|stall)s?", "alternative": "birthing cage", "reason": "Industry euphemism for the metal cage confining a sow during birth and nursing. 'Birthing cage' is accurate."},
    {"regex": r"battery[\s-]cage[ds]?", "alternative": "small wire cage", "reason": "Industry euphemism for wire enclosures that give each hen less floor space than a sheet of paper. 'Small wire cage' describes what it is."},
    {"regex": r"spent\s+hens?", "alternative": "hen killed after egg production declines", "reason": "'Spent' frames the hen as a depleted resource. Naming what actually happens — she is killed when her egg production falls — is more accurate."},
    {"regex": r"humane(ly)?\s+(slaughter(ed)?|killing|death)", "alternative": "slaughter", "reason": "Industry oxymoron — a killing cannot be 'humane' to the one being killed. Drop the modifier and use 'slaughter' or 'killing.'"},
    {"regex": r"\b(?:broiler\s+(chickens?|hens?)|broilers)\b", "alternative": "chicken raised for meat", "reason": "Industry term that defines a chicken by its commercial purpose. 'Chicken raised for meat' is the human-readable version. (The kitchen appliance is not flagged.)"},
    {"regex": r"don'?t\s+be\s+a\s+chicken", "alternative": "don't hesitate", "reason": "Uses a chicken as an insult for cowardice. 'Don't hesitate' or 'be brave' is direct and doesn't rely on a demeaning stereotype."},
    {"regex": r"\b(?:badger(ed|ing|s)?)\b", "alternative": "pester", "reason": "Comes from badger-baiting, a blood sport where dogs were set on captive badgers. 'Pester' or 'pressure' carries the same meaning without the origin."},
    {"regex": r"\b(?:ferret(ed|ing)?\s+out)\b", "alternative": "uncover", "reason": "Refers to the historical use of ferrets to flush rabbits out of burrows to be killed. 'Uncover' or 'dig up' works just as well."},
    {"regex": r"cattle[,]?\s+(not|vs\.?|versus)\s+pets|pets\s+not\s+cattle", "alternative": "ephemeral vs. persistent", "reason": "Infrastructure metaphor that Google's own style guide flags for removal as 'figurative language that relates to the slaughter of animals.' 'Ephemeral vs. persistent' or 'disposable vs. unique' captures the same architectural concept."},
    {"regex": r"canary\s+in\s+(a|the)\s+coal\s+mine", "alternative": "early warning signal", "reason": "Refers to canaries historically placed in coal mines to die first as a warning to miners. 'Early warning signal' or 'sentinel' conveys the meaning without the harm."},
    {"regex": r"fishing\s+expeditions?", "alternative": "exploratory investigation", "reason": "Frames speculative inquiry as fishing — the metaphor softens the catch. 'Exploratory investigation' is clearer, especially in legal writing."},
    {"regex": r"\b(?:sacred\s+cows?)\b", "alternative": "unquestioned belief", "reason": "Treats cattle as objects in an 'untouchable' metaphor while also trivializing Hindu beliefs. 'Unquestioned belief' or 'protected assumption' avoids both issues."},
    {"regex": r"\b(?:scapegoat(ed|ing|s)?)\b", "alternative": "blame target", "reason": "Originates from the ritual sacrifice of goats to carry away blame. 'Blame target' or 'wrongly blamed' is more precise."},
    {"regex": r"dead[\s_-]?cat[\s_-]?bounce", "alternative": "temporary rebound", "reason": "A financial term built on the image of a dead cat. 'Temporary rebound' or 'false recovery' is more professional and avoids the image."},
    {"regex": r"\b(?:dog[\s-]eat[\s-]dog)\b", "alternative": "ruthlessly competitive", "reason": "Frames dogs as inherently violent toward each other as a model for competition. 'Ruthlessly competitive' or 'cutthroat' conveys the meaning without the stereotype."},
    {"regex": r"\b(?:whack[\s-]a[\s-]mole)\b", "alternative": "recurring problem", "reason": "References a game built around repeatedly striking animals as they pop up. 'Recurring problem' or 'endless loop' describes the pattern more precisely."},
    {"regex": r"cash\s+cows?", "alternative": "moneymaker", "reason": "Treats a cow as a thing to be extracted from for profit. 'Moneymaker' or 'profit center' carries the same meaning."},
    {"regex": r"\b(?:sacrificial\s+lambs?)\b", "alternative": "expendable person", "reason": "References the ritual slaughter of lambs. 'Expendable person' or 'someone sacrificed for others' communicates the metaphor directly."},
    {"regex": r"\b(?:sitting\s+ducks?)\b", "alternative": "easy target", "reason": "Hunting imagery — a duck in the open, easy to shoot. 'Easy target' or 'vulnerable target' says the same thing."},
    {"regex": r"\b(?:open\s+season)\b", "alternative": "free-for-all", "reason": "Refers to the legal hunting period when killing animals is permitted. 'Free-for-all' or 'no holds barred' conveys the meaning without the hunting framing."},
    {"regex": r"put(s|ting)?(\s+(him|her|them))?\s+out\s+to\s+pasture", "alternative": "retire", "reason": "Refers to the farm practice of disposing of animals once they're no longer productive. 'Retire,' 'phase out,' or 'sunset' is clearer and carries no harm."},
    {"regex": r"\b(?:dead\s+ducks?)\b", "alternative": "lost cause", "reason": "Hunting imagery — a duck that has been shot and killed. 'Lost cause' or 'doomed effort' is just as expressive."},
    {"regex": r"\b(?:cull(ed|ing|s)?)\b", "alternative": "remove", "reason": "Euphemism used in wildlife management and farming for mass killing. 'Remove', 'prune', 'trim', or 'filter out' is accurate in technical contexts."},
    {"regex": r"\b(?:veal(\s+cal(f|ves))?)\b", "alternative": "calf flesh", "reason": "'Veal' softens 'slaughtered-calf flesh' via a Norman-French borrowing. In advocacy or industry-critical writing, 'calf flesh' names what it is. (Suppressed in recipes and cooking contexts.)"},
    {"regex": r"\b(?:lame[\s-]duck)\b", "alternative": "outgoing", "reason": "Combines an ableist adjective with a reference to a bird unable to fly due to injury. 'Outgoing', 'transitional', or 'ineffective' is more precise."},
    {"regex": r"\b(?:debeak(ing|ed)|beak\s+(trimming|trim|conditioning))\b", "alternative": "beak amputation", "reason": "Industry euphemism for slicing or burning off hens' beaks, typically without anesthesia. 'Beak amputation' names what actually happens."},
    {"regex": r"\b(?:dehorn(ing|ed)|disbud(ding|ded))\b", "alternative": "horn amputation", "reason": "Industry term for removing cattle horns, typically without anesthesia. 'Horn amputation' is accurate."},
    {"regex": r"tail[\s-]docking|tail\s+docked|docked\s+tail", "alternative": "tail amputation", "reason": "Amputating pigs', sheep's, or dogs' tails. 'Tail amputation' is the accurate term."},
    {"regex": r"ear[\s-]notch(ing|ed)", "alternative": "ear mutilation", "reason": "Industry identification practice of cutting notches in animals' ears. 'Ear mutilation' names what it is."},
    {"regex": r"ventilation\s+shutdown(\s+plus)?|VSD\+|VSD\s+plus", "alternative": "mass killing by suffocation", "reason": "Industry term for killing entire flocks by cutting off airflow — the animals die from suffocation and heat. 'Mass killing by suffocation' is the accurate term. (Suppressed in HVAC contexts.)"},
    {"regex": r"(maceration\s+of\s+chicks|chick\s+maceration|macerat(ed|ing)\s+chicks)", "alternative": "grinding newborn chicks alive", "reason": "Industry euphemism for killing day-old male chicks by grinding them alive. Say what the process is. (Bare 'maceration' in culinary or chemistry contexts is not flagged.)"},
    {"regex": r"\b(?:abattoirs?)\b", "alternative": "slaughterhouse", "reason": "French-derived euphemism for slaughterhouse. 'Slaughterhouse' is the accurate English term."},
    {"regex": r"rendering\s+(plant|facility)s?", "alternative": "animal-body processing plant", "reason": "Facility that processes animal bodies — roadkill, downed animals, slaughter byproducts — into meal, fat, and tallow. Naming it accurately makes the supply chain visible. (Only the full compound 'rendering plant' / 'rendering facility' is flagged; bare 'rendering' for graphics or UI is not.)"},
    {"regex": r"\b(?:stockyards?)\b", "alternative": "slaughterhouse pens", "reason": "Euphemism for pre-slaughter holding pens. 'Slaughterhouse pens' describes what the facility actually is."},
    {"regex": r"(laying|layer)\s+hens?", "alternative": "hen", "reason": "Defines a hen by her egg-laying function. When sex and species are relevant, 'hen' is sufficient."},
    {"regex": r"(dairy|beef)\s+(cow|cows|cattle)|meat\s+(birds?|rabbits?|goats?)", "alternative": "cow", "reason": "Defines an animal by the product humans extract from them. The species name alone is sufficient unless the use is actively relevant."},
    {"regex": r"brood\s+sows?|breeding\s+(stock|pair)", "alternative": "pregnant pig", "reason": "Defines a female animal by her reproductive function. Name the individual directly where possible."},
    {"regex": r"cattle\s+calls?", "alternative": "open call", "reason": "Likens human applicants to livestock being herded. 'Open call' or 'mass audition' carries the same meaning without the framing."},
    {"regex": r"pet\s+projects?", "alternative": "side project", "reason": "Carries over the property framing of 'pet' (something owned) to the project. 'Side project' or 'passion project' captures the same idea without the ownership framing."},
    {"regex": r"humanely\s+(raised|produced|farmed)", "alternative": "factory-farmed", "reason": "USDA-unregulated marketing label — companies define their own standards, and the actual conditions often differ little from factory farming. Describe the actual conditions where possible."},
    {"regex": r"free[\s-]rang(e|ing)|free[\s-]roaming", "alternative": "minimally accessible outdoor pen", "reason": "USDA requires only 'access to outdoors' — often a small door to a small porch that most birds never use. The label does not guarantee meaningful outdoor life."},
    {"regex": r"pasture[\s-]raised|pastured", "alternative": "raised on pasture (certifier-dependent)", "reason": "Not USDA-regulated; the meaning depends on whichever certifier the producer chooses. Name the certifier and the actual conditions where possible."},
    {"regex": r"grass[\s-](fed|finished)", "alternative": "grass-fed (USDA definition dropped 2016)", "reason": "Describes the cattle's feed, not their welfare. Slaughter, transport, and mother-calf separation happen the same way. The USDA dropped its 'grass-fed' definition in 2016; current usage is producer-defined."},
    {"regex": r"cage[\s-]free\s+(chicken|turkey|meat|pork|beef)", "alternative": "crowded indoor housing", "reason": "Meaningless for meat birds — broiler chickens and turkeys are almost never caged in industrial production. The label implies a welfare improvement that doesn't exist. (Cage-free for eggs IS a meaningful distinction; that usage is not flagged.)"},
    {"regex": r"Certified\s+Humane|Animal\s+Welfare\s+Approved|Global\s+Animal\s+Partnership|American\s+Humane\s+Certified|One\s+Health\s+Certified|GAP\s+(certified|Step(\s+\d)?)", "alternative": "name the certifier and standard", "reason": "Third-party welfare certifications with widely varying standards — some are meaningful (Animal Welfare Approved), others are marketing (American Humane Certified). Name the specific standard if relevant."},
    {"regex": r"(ethically|responsibly)\s+sourced\s+(meat|dairy|eggs|beef|pork|chicken)|happy\s+(meat|cows?)", "alternative": "describe the actual farm practices", "reason": "Marketing language without a standard definition when applied to animal products. 'Ethically sourced' meat has no USDA definition. Describe the actual practices instead. (The phrase applied to coffee, chocolate, or textiles is not flagged.)"},
    {"regex": r"dolphin[\s-]safe|line[\s-]caught|pole[\s-](and[\s-]line[\s-])?caught|sustainab(ly\s+caught|le\s+seafood)", "alternative": "name the specific fishing method and bycatch statistics", "reason": "Addresses specific bycatch concerns but not fish suffering. Fish feel pain, suffocate on deck, or are crushed in nets regardless of how the boat avoids catching dolphins or catches fish one at a time."},
    {"regex": r"(feed|fed|feeding)\s+to\s+the\s+(lions|sharks|dogs)", "alternative": "sacrifice", "reason": "Human-as-prey imagery. 'Sacrifice' or 'leave exposed' captures the same meaning."},
    {"regex": r"(like\s+(a\s+)?)?pigs?\s+to\s+slaughter", "alternative": "defenseless", "reason": "Direct slaughter imagery. 'Defenseless' or 'walking into disaster' captures the same meaning."},
    {"regex": r"turkey[\s-]shoot", "alternative": "trivially easy win", "reason": "One-sided-slaughter imagery for an easy win. 'Walkover' or 'trivially easy win' carries the same meaning."},
    {"regex": r"fox(es)?\s+(guarding\s+the|in\s+the)\s+hen[\s-]?house", "alternative": "conflict of interest", "reason": "Frames predation as an inevitable natural order. 'Conflict of interest' or 'wrong person in charge' is the actual point being made."},
    {"regex": r"(like\s+a\s+)?bull\s+in\s+a\s+china\s+shop", "alternative": "tornado in a glass factory", "reason": "Bull-as-clumsy-brute stereotype — actually originates from a cartoon, not reality. 'Clumsy disruption' or 'careless and destructive' is more accurate."},
    {"regex": r"build(s|ing)?\s+a\s+better\s+mousetrap|better\s+mousetrap", "alternative": "build a better mouse pad", "reason": "Mouse-killing device as innovation metaphor. 'Invent something better' or 'build a better mouse pad' captures the idea."},
    {"regex": r"(packed|squeezed)\s+(in\s+)?like\s+sardines", "alternative": "packed in like pickles", "reason": "Accurately describes industrial fishing and canning — the 'imagery' is the reality. 'Tightly crowded' or 'packed in like pickles' works without invoking it."},
    {"regex": r"pull(s|ing|ed)?\s+the\s+wool\s+over", "alternative": "deceive", "reason": "Wool (sheep exploitation) as a deception metaphor. 'Deceive' or 'mislead' is direct and clearer."},
    {"regex": r"(put(s|ting)?\s+)?lipstick\s+on\s+a\s+pig", "alternative": "superficially improve", "reason": "Frames pigs as ugly objects. 'Superficially improve' or 'disguise the flaw' is the actual meaning."},
    {"regex": r"silk\s+purse\s+(out\s+of|from)\s+a\s+sow's\s+ear", "alternative": "diamond bracelet out of a lump of coal", "reason": "Pig body parts framed as worthless. 'Transform something unpromising' carries the same meaning."},
    {"regex": r"black\s+sheep", "alternative": "outlier", "reason": "Commodifies sheep coat color as a family-shame metaphor, with racial baggage. 'Outlier' or 'odd one out' works."},
    {"regex": r"wol(f|ves)\s+in\s+sheep'?s\s+clothing", "alternative": "deceiver in disguise", "reason": "Wolves-as-deceivers trope. 'Hidden threat' or 'deceiver in disguise' carries the same meaning."},
    {"regex": r"chicken(s|ed|ing)\s+out|chicken\s+out", "alternative": "back out", "reason": "Chicken-as-coward framing. 'Back out' or 'lose nerve' carries the same meaning."},
    {"regex": r"feeding\s+frenz(y|ies)", "alternative": "chaotic rush", "reason": "Shark-predation imagery used for human behavior. 'Chaotic rush' or 'scramble to exploit' carries the same meaning."},
    {"regex": r"(smell[s]?\s+)?blood\s+in\s+the\s+water", "alternative": "signs of weakness", "reason": "Shark-predation imagery. 'Signs of weakness' or 'vulnerability visible' carries the same meaning."},
    {"regex": r"(circl(e|ing)\s+(like\s+)?vultures|vultures\s+circling)", "alternative": "waiting to exploit", "reason": "Species defamation — the 'circling vulture' framing is factually wrong (vultures are ecological cleaners, not predators) and has driven real persecution; vulture populations are crashing globally. 'Waiting to exploit' carries the same meaning."},
    {"regex": r"mad(der)?\s+(than|as)\s+a\s+wet\s+hen", "alternative": "furious", "reason": "References the farm practice of dunking broody hens in water to break their nesting instinct. 'Furious' or 'livid' says it directly."},
    {"regex": r"code\s+monkeys?", "alternative": "developer", "reason": "Frames programmers as trained animals, and compounds with the long history of 'monkey' used as a racial slur. 'Developer' or 'engineer' is the accurate term."},
    {"regex": r"(memory|CPU|bandwidth|resource|disk|space)\s+hog|hogging\s+(memory|CPU|bandwidth|resources|the)|hogs\s+the|hog\s+the\s+spotlight", "alternative": "resource-intensive", "reason": "Builds on the pig-as-greedy stereotype (pigs are actually selective eaters). 'Resource-intensive' or 'monopolizes' is more accurate and avoids the framing."},
    {"regex": r"\b(?:pig[\s-]?headed(ness)?)\b", "alternative": "obstinate", "reason": "Pig-as-stubborn stereotype (pigs are intelligent, not stubborn). 'Obstinate' or 'unreasonable' says it directly."},
    {"regex": r"eat(s|ing|e)?\s+like\s+a\s+pig|ate\s+like\s+a\s+pig|pig(s|ged|ging)?\s+out", "alternative": "overeat", "reason": "Pig-as-glutton stereotype (actually wrong — pigs are selective eaters in natural conditions). 'Overeat' or 'gorge' says the same thing."},
    {"regex": r"sons?[\s-]of[\s-]a[\s-]bitch|sons\s+of\s+bitches", "alternative": "specific descriptor", "reason": "Female-dog insult that compounds misogyny with species defamation. A specific descriptor is clearer and doesn't land on anyone's mother or on dogs."},
    {"regex": r"\b(?:sheeple)\b", "alternative": "conformists", "reason": "Coined term meaning 'sheep-people' — dehumanizes the target while defaming sheep (who are actually complex social animals). 'Conformists' or 'uncritical crowd' carries the same meaning."},
    {"regex": r"(loan|card)[\s-]sharks?", "alternative": "predatory lender", "reason": "Species-as-predator trope applied to exploitative humans, which misrepresents sharks and provides a convenient framing for financial harm. 'Predatory lender' or 'hustler' is direct and more accurate."},
    {"regex": r"vulture\s+(capitalist|capitalism|fund)s?", "alternative": "predatory investor", "reason": "Species defamation that drives real-world vulture persecution — global vulture populations are crashing largely from this kind of cultural framing. 'Predatory investor' names the behavior without defaming an ecologically critical species."},
    {"regex": r"weasel\s+words?|weasel(s|ed|ing)?\s+out", "alternative": "evasive language", "reason": "Species-as-deceitful trope. 'Evasive language' or 'slippery phrasing' is more direct. (Wikipedia's Manual of Style uses 'weasel words' as an internal term of art; that context is suppressed.)"},
    {"regex": r"leech(es|ed|ing)?\s+off|bloodsuckers?", "alternative": "freeload", "reason": "Species-as-parasite trope. 'Freeload' or 'mooch' is direct. (Bare 'leech' in medical contexts — leeches are still used in some surgeries — is not flagged.)"},
    {"regex": r"monkey\s+business|monkey(s|ing|ed)?\s+around|(make|makes|making|made)\s+a\s+monkey\s+of", "alternative": "mischief", "reason": "Primate-as-foolish stereotype with a long racial history. 'Mischief' or 'fool around' is direct and doesn't carry the baggage."},
    {"regex": r"not\s+my\s+(circus[,]?\s+not\s+my\s+monkeys?|monkeys?|circus)", "alternative": "not my problem", "reason": "Direct reference to circus-animal exploitation. 'Not my problem' carries the same meaning."},
    {"regex": r"\b(?:bird[\s-]?brain(ed)?)\b", "alternative": "forgetful", "reason": "Bird-as-stupid stereotype (corvids and parrots rank among the most cognitively sophisticated non-human animals). 'Forgetful' or 'absent-minded' is more accurate."},
    {"regex": r"foie[\s-]gras", "alternative": "force-fed duck liver", "reason": "French for 'fat liver'; obscures that the product comes from force-feeding ducks or geese until their livers enlarge to ten times normal size. Name the process."},
    {"regex": r"\b(?:chevon)\b", "alternative": "goat flesh", "reason": "Marketing-constructed word (coined in the 1920s) to make goat meat palatable to Anglophone consumers. 'Goat flesh' or 'goat meat' is accurate."},
    {"regex": r"\b(?:sweetbreads?)\b", "alternative": "calf thymus", "reason": "Opaque culinary term for calf or lamb thymus or pancreas. Naming the organ is clearer. (Suppressed in recipe/cooking contexts.)"},
    {"regex": r"\b(?:mutton)\b", "alternative": "sheep flesh", "reason": "'Mutton' obscures the species. 'Sheep flesh' names it. (Suppressed in recipe contexts.)"},
    {"regex": r"\b(?:venison)\b", "alternative": "deer flesh", "reason": "'Venison' obscures the species. 'Deer flesh' names it. (Suppressed in recipe or hunting-regulation contexts.)"},
    {"regex": r"\b(?:squabs?)\b", "alternative": "pigeon flesh", "reason": "Marketing term for young pigeon raised for slaughter. 'Pigeon flesh' names what it is. (Suppressed in recipe contexts.)"},
    {"regex": r"\b(?:spare[\s-]?ribs)\b", "alternative": "pig ribs", "reason": "'Spare' frames body parts as disposable/extra. 'Pig ribs' is accurate. (Suppressed in recipe/BBQ contexts.)"},
    {"regex": r"\b(?:(genuine|real|top[\s-]grain|full[\s-]grain)?\s*leather)\b", "alternative": "cow skin", "reason": "'Leather' obscures that the material is the skin of a killed cow (or pig, sheep, etc.). In advocacy or supply-chain writing, naming it is clearer. Suppressed in fashion/product contexts where the industry term is expected."},
    {"regex": r"\b(?:(merino\s+|lambs)?wool)\b", "alternative": "sheep hair", "reason": "'Wool' obscures that the fiber is sheep hair, usually from sheep bred for extreme coat yields (mulesing, shearing injury, eventual slaughter). Advocacy writing names it directly. Suppressed in textile/fashion contexts."},
    {"regex": r"down\s+(feathers|jacket|comforter|pillow|filling)|(goose|duck)\s+down", "alternative": "plant-based insulation", "reason": "Down is plucked from ducks and geese, often while alive and distressed. 'Plant-based insulation' or 'synthetic fill' describes the alternative. Bare 'down' (direction) is NOT flagged — only product compounds."},
    {"regex": r"\b(?:cashmere|mohair|angora)\b", "alternative": "goat hair", "reason": "Luxury-marketing names that obscure the animal source. Cashmere and mohair come from goats; angora comes from rabbits (who are often plucked live and injured). Naming the species is clearer in advocacy writing."},
    {"regex": r"\b(?:(pure\s+|mulberry\s+|raw\s+)?silk)\b", "alternative": "plant silk", "reason": "Silk production typically requires boiling silkworms alive inside their cocoons to prevent the thread from breaking. Peace silk, plant silk, and synthetics avoid this. Suppressed in textile/fashion contexts."},
    {"regex": r"royal\s+jelly|beeswax|propolis", "alternative": "plant alternative", "reason": "Bee products are extracted through industrial beekeeping, which involves queen-clipping, smoke stressing, and often the destruction of hives. Plant-based waxes (candelilla, carnauba, soy) serve most of the same purposes."},
    {"regex": r"down(ed|er)\s+(animal|cow|cattle|pig)s?", "alternative": "animal too sick or injured to walk", "reason": "'Downed' uses passive voice to elide why the animal is on the ground — untreated injury or illness in transport or on the farm. 'Too sick to walk' names the condition."},
    {"regex": r"(artificial|forced)\s+insemination|AI\s+in\s+(cattle|cows|dairy|pigs|sheep|swine)", "alternative": "forced impregnation", "reason": "Industry-standard procedure involving restraint and reproductive invasion. 'Forced impregnation' is the accurate term when the animal cannot consent. (The bare abbreviation 'AI' is not flagged — too much overlap with artificial intelligence. The rule fires only on the specific animal-ag compounds.)"},
    {"regex": r"\b(?:farrow(ing|ed))\b", "alternative": "giving birth (for pigs)", "reason": "Industry verb that erases the individual animal giving birth. 'Giving birth' is the plain-language version. (The compound 'farrowing crate' is flagged by its own rule.)"},
    {"regex": r"live\s+(export(s|ing)?|transport|shipment)", "alternative": "transport to slaughter", "reason": "Industry term for loading animals onto ships or trucks for days-to-weeks journeys to overseas slaughter. 'Transport to slaughter' names the destination."},
    {"regex": r"(pork|beef|dairy|poultry|veal|egg)\s+industry", "alternative": "pig-flesh industry", "reason": "Each term names the product rather than the species it comes from. Naming the species (e.g. 'pig-flesh industry') makes the supply chain visible. Low priority — use in advocacy writing, not general documentation."},
    {"regex": r"trophy\s+(hunt(ing|er|ers)?|kill(s)?)", "alternative": "killing for display", "reason": "Frames a killed animal as an achievement to be displayed. 'Killing for display' or 'recreational killing' names the activity."},
    {"regex": r"big[\s-]game\s+hunt(ing|er|ers)?", "alternative": "large-animal hunter", "reason": "'Big game' frames large wild animals as sport objects existing for human recreation. 'Large-animal hunter' names it; better still, name the species (elephant, lion, rhino)."},
    {"regex": r"sport[\s]?fishing|recreational\s+fishing|game\s+fishing", "alternative": "recreational fishing (if literal)", "reason": "'Sport' frames killing fish as leisure. In contexts critical of the activity, 'recreational killing of fish' is accurate. (In neutral angling-industry writing, the scanner adds noise; tune the context or disable in those files.)"},
    {"regex": r"catch[\s-]and[\s-]release", "alternative": "capture and release", "reason": "Frames hook injury, exhaustion, and stress as harmless. Studies show significant post-release mortality, especially for species caught from deep water. 'Capture and release' is more neutral."},
    {"regex": r"thin(s|ning|ned)?\s+(out\s+)?the\s+herd", "alternative": "reduce numbers by killing", "reason": "Culling euphemism that softens 'kill off selected animals.' 'Kill off' says it directly."},
    {"regex": r"humane\s+(traps?|removal|control)", "alternative": "non-lethal trap", "reason": "'Humane' sanitizes the practice. Say whether it's lethal or non-lethal directly — 'non-lethal trap' is clearer and testable."},
    {"regex": r"lethal\s+(removal|control|management)", "alternative": "killing program", "reason": "Bureaucratic language for killing programs. 'Killing program' says it plainly."},
    {"regex": r"(fur|mink|fox)\s+(farms?|ranch(es)?)", "alternative": "mink confinement facility", "reason": "'Farm' or 'ranch' evokes pastoral imagery; these are intensive confinement facilities where animals live in wire cages before being gassed or electrocuted. Name them directly."},
    {"regex": r"fur[\s-]bearing\s+animals?", "alternative": "named species", "reason": "Defines wild animals by a human use. Naming the species (foxes, minks, coyotes, bobcats, chinchillas) is clearer."},
    {"regex": r"\b(?:by[\s-]?catch)\b", "alternative": "incidental killing", "reason": "Neutralizes the massive incidental killing of non-target marine species — hundreds of thousands of dolphins, sea turtles, seabirds, and sharks each year. 'Incidental killing' names it."},
    {"regex": r"fish(ery)?\s+stocks?", "alternative": "fish populations", "reason": "Commodity framing of marine life as a renewable resource. 'Fish populations' is neutral and accurate."},
    {"regex": r"\b(?:aquaculture|fish\s+farming)\b", "alternative": "industrial fish farming", "reason": "Neutral-sounding framing for intensive fish confinement and slaughter. In advocacy writing, 'industrial fish farming' is more accurate."},
    {"regex": r"cr(y|ied|ying|ies)\s+wolf", "alternative": "raise false alarms", "reason": "Rooted in Aesop's fable, the phrase reinforces the wolf-as-menace framing that has driven centuries of wolf persecution. 'Raise false alarms' captures the meaning."},
    {"regex": r"pecking\s+orders?", "alternative": "hierarchy", "reason": "Derived from the actual behavior of hens in confinement, where crowding causes injurious pecking. 'Hierarchy' or 'chain of command' captures the same idea."},
    {"regex": r"play(s|ing|ed)?\s+cat\s+and\s+mouse|(cat\s+and\s+mouse\s+game|game\s+of\s+cat\s+and\s+mouse)", "alternative": "drawn-out pursuit", "reason": "Predator-prey torture metaphor — the game is about prolonging the suffering. 'Drawn-out pursuit' captures the meaning."},
    {"regex": r"cat\s+(that|who)\s+(swallowed|ate)\s+the\s+canary|canary[\s-]eating\s+grin", "alternative": "smug with secret knowledge", "reason": "Predation imagery — a dead canary is the joke's punchline. 'Smug with secret knowledge' captures it."},
    {"regex": r"(chomping|champing|chomps|champs)\s+at\s+the\s+bit", "alternative": "eager to start", "reason": "References the metal 'bit' forced into a horse's mouth; the phrase describes the horse's attempt to relieve it. 'Eager to start' says the same thing."},
    {"regex": r"whip(s|ped|ping)?\s+into\s+shape", "alternative": "get organized", "reason": "Whip-violence imagery from animal training. 'Get organized' or 'restore order' is direct. (Political 'whip' and culinary 'whip' — different usage — are suppressed.)"},
    {"regex": r"whal(e|es|ing|ed)\s+on", "alternative": "pummel", "reason": "Whaling (whale slaughter) as metaphor for repeated hitting. 'Pummel' or 'hammer' is direct."},
    {"regex": r"fish\s+or\s+cut\s+bait", "alternative": "decide", "reason": "Fishing imagery. 'Decide' or 'commit or move on' is direct."},
    {"regex": r"pull(s|ing|ed)?\s+a\s+rabbit\s+out\s+of\s+a\s+hat", "alternative": "pull a coin out of an ear", "reason": "Stage magic often uses live rabbits kept in distressing conditions. 'Magically solve' or 'produce unexpectedly' carries the meaning without referencing the practice."},
    {"regex": r"walk(s|ing|ed)?\s+on\s+eggshells", "alternative": "walking on thin ice", "reason": "Commodifies eggs as fragile objects; erases the laying-hen origin. 'Walking on thin ice' carries the same meaning."},
    {"regex": r"put\s+(a|the)\s+\S+\s+out\s+of\s+(its|their|the)\s+misery|put\s+(it|them)\s+out\s+of\s+(its|their)\s+misery|put\s+out\s+of\s+(its|their|the)\s+misery", "alternative": "end the suffering", "reason": "Horse-killing idiom. 'End the suffering' carries the same meaning without the imagery."},
    {"regex": r"kill(ing)?\s+the\s+fatted\s+calf", "alternative": "celebrate grandly", "reason": "Biblical animal-sacrifice imagery (Luke 15 — the Prodigal Son). 'Celebrate grandly' or 'roll out the red carpet' carries the same meaning."},
    {"regex": r"(acting\s+like\s+lemmings|lemming\s+(investor|investors|behavior)|like\s+lemmings)", "alternative": "herd-following investor", "reason": "Based on a Disney hoax — the 1958 'White Wilderness' staged lemmings being driven off a cliff. Lemmings don't mass-suicide. The metaphor defames the species and misleads the reader."},
    {"regex": r"(you|little|filthy|dirty)\s+maggots?", "alternative": "specific descriptor", "reason": "Degrading insect insult. Most uses in documentation are quoting dialogue or user-generated content; otherwise, use a specific descriptor."},
    {"regex": r"(filthy|dirty|you|capitalist|fascist|bourgeois)\s+swine", "alternative": "specific descriptor", "reason": "Pig-as-degraded pejorative. Naming the actual trait (greedy, exploitative, corrupt) is clearer. (Bare 'swine' in medical contexts like 'swine flu' is not flagged.)"},
    {"regex": r"\b(?:cat[\s-]?fights?)\b", "alternative": "heated argument", "reason": "Gendered insult — almost exclusively applied to women arguing, framing them as cats fighting. 'Heated argument' or 'altercation' is neutral."},
    {"regex": r"(humans?\s+and\s+animals|animals\s+and\s+(humans?|people)|people\s+and\s+animals|man\s+and\s+beast)", "alternative": "humans and non-human animals", "reason": "False dichotomy — humans ARE animals. The phrasing reproduces the speciesist framing animal-liberation writing opposes. 'Humans and other animals' preserves the meaning accurately."},
    {"regex": r"(pet|dog|cat|rabbit|bird)\s+owners?", "alternative": "pet guardian", "reason": "Property framing — 'owner' treats sentient beings as possessions. 'Guardian' preserves the legal and caregiving relationship without the property connotation. Used in legal reform jurisdictions (e.g. Boulder CO, West Hollywood) since the early 2000s."},
    {"regex": r"own(s|ing|ed)?\s+a\s+(pet|dog|cat|rabbit|bird)", "alternative": "live with a companion animal", "reason": "Property framing applied to companion animals. 'Live with a dog' or 'share a home with a cat' captures the relationship without the ownership frame."},
]

COMPILED = [
    (re.compile(p["regex"], re.IGNORECASE), p["alternative"], p["reason"])
    for p in PATTERNS
]


def check_file(filepath):
    """Check a single file for animal violence language. Returns list of findings."""
    findings = []
    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            for line_num, line in enumerate(f, start=1):
                for regex, alternative, reason in COMPILED:
                    for match in regex.finditer(line):
                        findings.append(
                            (filepath, line_num, match.group(), alternative, reason)
                        )
    except (OSError, IOError):
        pass
    return findings


def main():
    """Entry point. Accepts filenames as arguments (provided by pre-commit)."""
    filenames = sys.argv[1:]
    if not filenames:
        return 0

    all_findings = []
    for filename in filenames:
        all_findings.extend(check_file(filename))

    if all_findings:
        print("Animal violence language detected:\n")
        for filepath, line_num, matched, alternative, reason in all_findings:
            print(f"  {filepath}:{line_num}")
            print(f'    Found:   "{matched}"')
            print(f'    Suggest: "{alternative}"')
            print(f"    Why:     {reason}\n")
        print(
            f"{len(all_findings)} instance(s) found. "
            "Consider using the suggested alternatives."
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
