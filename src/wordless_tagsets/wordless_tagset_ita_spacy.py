#
# Wordless: Tagsets - spaCy Italian Tagset
#
# Copyright (C) 2018-2019  Ye Lei (叶磊)
#
# This source file is licensed under GNU GPLv3.
# For details, see: https://github.com/BLKSerene/Wordless/blob/master/LICENSE.txt
#
# All other rights reserved.
#

#
# spaCy Italian Tagset: https://github.com/explosion/spaCy/blob/master/spacy/lang/it/tag_map.py
#
# Universal POS Tags: http://universaldependencies.org/u/pos/all.html
#

mappings = [
    ['AP__Gender=Fem|Number=Plur|Poss=Yes|PronType=Prs', 'DET', '', ''],
    ['AP__Gender=Fem|Number=Sing|Poss=Yes|PronType=Prs', 'DET', '', ''],
    ['AP__Gender=Masc|Number=Plur|Poss=Yes|PronType=Prs', 'DET', '', ''],
    ['AP__Gender=Masc|Number=Sing|Poss=Yes|PronType=Prs', 'DET', '', ''],
    ['AP__Gender=Masc|Poss=Yes|PronType=Prs', 'DET', '', ''],
    ['AP__Number=Sing|Poss=Yes|PronType=Prs', 'DET', '', ''],
    ['AP__Poss=Yes|PronType=Prs', 'DET', '', ''],

    ['A__Degree=Abs|Gender=Fem|Number=Plur', 'ADJ', '', ''],
    ['A__Degree=Abs|Gender=Fem|Number=Sing', 'ADJ', '', ''],
    ['A__Degree=Abs|Gender=Masc|Number=Plur', 'ADJ', '', ''],
    ['A__Degree=Abs|Gender=Masc|Number=Sing', 'ADJ', '', ''],
    ['A__Degree=Cmp', 'ADJ', '', ''],
    ['A__Degree=Cmp|Number=Plur', 'ADJ', '', ''],
    ['A__Degree=Cmp|Number=Sing', 'ADJ', '', ''],
    ['A__Gender=Fem|Number=Plur', 'ADJ', '', ''],
    ['A__Gender=Fem|Number=Sing', 'ADJ', '', ''],
    ['A__Gender=Fem|Number=Sing|Poss=Yes|PronType=Prs', 'ADJ', '', ''],
    ['A__Gender=Masc', 'ADJ', '', ''],
    ['A__Gender=Masc|Number=Plur', 'ADJ', '', ''],
    ['A__Gender=Masc|Number=Sing', 'ADJ', '', ''],
    ['A__Number=Plur', 'ADJ', '', ''],
    ['A__Number=Sing', 'ADJ', '', ''],
    ['A___', 'ADJ', '', ''],

    ['BN__PronType=Neg', 'ADV', '', ''],

    ['B__Degree=Abs', 'ADV', '', ''],
    ['B__Degree=Abs|Gender=Masc|Number=Sing', 'ADV', '', ''],
    ['B___', 'ADV', '', ''],

    ['CC___', 'CCONJ', '', ''],

    ['CS___', 'SCONJ', '', ''],

    ['DD__Gender=Fem|Number=Plur|PronType=Dem', 'DET', '', ''],
    ['DD__Gender=Fem|Number=Sing|PronType=Dem', 'DET', '', ''],
    ['DD__Gender=Masc|Number=Plur|PronType=Dem', 'DET', '', ''],
    ['DD__Gender=Masc|Number=Sing|PronType=Dem', 'DET', '', ''],
    ['DD__Gender=Masc|PronType=Dem', 'DET', '', ''],
    ['DD__Number=Plur|PronType=Dem', 'DET', '', ''],
    ['DD__Number=Sing|PronType=Dem', 'DET', '', ''],

    ['DE__PronType=Exc', 'DET', '', ''],

    ['DI__Definite=Def|Gender=Fem|Number=Plur|PronType=Art', 'DET', '', ''],
    ['DI__Gender=Fem|Number=Plur', 'DET', '', ''],
    ['DI__Gender=Fem|Number=Plur|PronType=Ind', 'DET', '', ''],
    ['DI__Gender=Fem|Number=Sing|PronType=Ind', 'DET', '', ''],
    ['DI__Gender=Masc|Number=Plur', 'DET', '', ''],
    ['DI__Gender=Masc|Number=Plur|PronType=Ind', 'DET', '', ''],
    ['DI__Gender=Masc|Number=Sing|PronType=Ind', 'DET', '', ''],
    ['DI__Number=Sing|PronType=Art', 'DET', '', ''],
    ['DI__Number=Sing|PronType=Ind', 'DET', '', ''],
    ['DI__PronType=Ind', 'DET', '', ''],

    ['DQ__Gender=Fem|Number=Plur|PronType=Int', 'DET', '', ''],
    ['DQ__Gender=Fem|Number=Sing|PronType=Int', 'DET', '', ''],
    ['DQ__Gender=Masc|Number=Plur|PronType=Int', 'DET', '', ''],
    ['DQ__Gender=Masc|Number=Sing|PronType=Int', 'DET', '', ''],
    ['DQ__Number=Plur|PronType=Int', 'DET', '', ''],
    ['DQ__Number=Sing|PronType=Int', 'DET', '', ''],
    ['DQ__PronType=Int', 'DET', '', ''],
    ['DQ___', 'DET', '', ''],

    ['DR__Number=Plur|PronType=Rel', 'DET', '', ''],
    ['DR__PronType=Rel', 'DET', '', ''],

    ['E__Gender=Masc|Number=Sing', 'ADP', '', ''],
    ['E___', 'ADP', '', ''],

    ['FB___', 'PUNCT', '', ''],

    ['FC___', 'PUNCT', '', ''],

    ['FF___', 'PUNCT', '', ''],

    ['FS___', 'PUNCT', '', ''],

    ['I__Polarity=Neg', 'INTJ', '', ''],
    ['I__Polarity=Pos', 'INTJ', '', ''],
    ['I___', 'INTJ', '', ''],

    ['NO__Gender=Fem|Number=Plur|NumType=Ord', 'ADJ', '', ''],
    ['NO__Gender=Fem|Number=Sing|NumType=Ord', 'ADJ', '', ''],
    ['NO__Gender=Masc|Number=Plur', 'ADJ', '', ''],
    ['NO__Gender=Masc|Number=Plur|NumType=Ord', 'ADJ', '', ''],
    ['NO__Gender=Masc|Number=Sing|NumType=Ord', 'ADJ', '', ''],
    ['NO__NumType=Ord', 'ADJ', '', ''],
    ['NO__Number=Sing|NumType=Ord', 'ADJ', '', ''],
    ['NO___', 'ADJ', '', ''],

    ['N__Gender=Masc|Number=Sing', 'NUM', '', ''],
    ['N__NumType=Card', 'NUM', '', ''],
    ['N__NumType=Range', 'NUM', '', ''],
    ['N___', 'NUM', '', ''],

    ['PART___', 'PART', '', ''],

    ['PC__Clitic=Yes|Definite=Def|Gender=Fem|Number=Plur|PronType=Art', 'PRON', '', ''],
    ['PC__Clitic=Yes|Gender=Fem|Number=Plur|Person=3|PronType=Prs', 'PRON', '', ''],
    ['PC__Clitic=Yes|Gender=Fem|Number=Plur|PronType=Prs', 'PRON', '', ''],
    ['PC__Clitic=Yes|Gender=Fem|Number=Sing|Person=3|PronType=Prs', 'PRON', '', ''],
    ['PC__Clitic=Yes|Gender=Fem|Person=3|PronType=Prs', 'PRON', '', ''],
    ['PC__Clitic=Yes|Gender=Masc|Number=Plur|Person=3|PronType=Prs', 'PRON', '', ''],
    ['PC__Clitic=Yes|Gender=Masc|Number=Sing|Person=3|PronType=Prs', 'PRON', '', ''],
    ['PC__Clitic=Yes|Gender=Masc|Number=Sing|PronType=Prs', 'PRON', '', ''],
    ['PC__Clitic=Yes|Number=Plur|Person=1|PronType=Prs', 'PRON', '', ''],
    ['PC__Clitic=Yes|Number=Plur|Person=2|PronType=Prs', 'PRON', '', ''],
    ['PC__Clitic=Yes|Number=Plur|Person=3|PronType=Prs', 'PRON', '', ''],
    ['PC__Clitic=Yes|Number=Plur|PronType=Prs', 'PRON', '', ''],
    ['PC__Clitic=Yes|Number=Sing|Person=1|PronType=Prs', 'PRON', '', ''],
    ['PC__Clitic=Yes|Number=Sing|Person=2|PronType=Prs', 'PRON', '', ''],
    ['PC__Clitic=Yes|Number=Sing|Person=3|PronType=Prs', 'PRON', '', ''],
    ['PC__Clitic=Yes|Person=3|PronType=Prs', 'PRON', '', ''],
    ['PC__Clitic=Yes|PronType=Prs', 'PRON', '', ''],

    ['PD__Gender=Fem|Number=Plur|PronType=Dem', 'PRON', '', ''],
    ['PD__Gender=Fem|Number=Sing|PronType=Dem', 'PRON', '', ''],
    ['PD__Gender=Masc|Number=Plur|PronType=Dem', 'PRON', '', ''],
    ['PD__Gender=Masc|Number=Sing|PronType=Dem', 'PRON', '', ''],
    ['PD__Number=Plur|PronType=Dem', 'PRON', '', ''],
    ['PD__Number=Sing|PronType=Dem', 'PRON', '', ''],
    ['PD__PronType=Dem', 'PRON', '', ''],

    ['PE__Gender=Fem|Number=Plur|Person=3|PronType=Prs', 'PRON', '', ''],
    ['PE__Gender=Fem|Number=Sing|Person=3|PronType=Prs', 'PRON', '', ''],
    ['PE__Gender=Masc|Number=Plur|Person=3|PronType=Prs', 'PRON', '', ''],
    ['PE__Gender=Masc|Number=Sing|Person=3|PronType=Prs', 'PRON', '', ''],
    ['PE__Number=Plur|Person=1|PronType=Prs', 'PRON', '', ''],
    ['PE__Number=Plur|Person=2|PronType=Prs', 'PRON', '', ''],
    ['PE__Number=Plur|Person=3|PronType=Prs', 'PRON', '', ''],
    ['PE__Number=Sing|Person=1|PronType=Prs', 'PRON', '', ''],
    ['PE__Number=Sing|Person=2|PronType=Prs', 'PRON', '', ''],
    ['PE__Number=Sing|Person=3|PronType=Prs', 'PRON', '', ''],
    ['PE__Person=3|PronType=Prs', 'PRON', '', ''],
    ['PE__PronType=Prs', 'PRON', '', ''],

    ['PI__Gender=Fem|Number=Plur|PronType=Ind', 'PRON', '', ''],
    ['PI__Gender=Fem|Number=Sing|PronType=Ind', 'PRON', '', ''],
    ['PI__Gender=Masc|Number=Plur|PronType=Ind', 'PRON', '', ''],
    ['PI__Gender=Masc|Number=Sing', 'PRON', '', ''],
    ['PI__Gender=Masc|Number=Sing|PronType=Ind', 'PRON', '', ''],
    ['PI__Number=Plur|PronType=Ind', 'PRON', '', ''],
    ['PI__Number=Sing|PronType=Ind', 'PRON', '', ''],
    ['PI__PronType=Ind', 'PRON', '', ''],

    ['PP__Gender=Fem|Number=Sing|Poss=Yes|PronType=Prs', 'PRON', '', ''],
    ['PP__Gender=Masc|Number=Plur|Poss=Yes|PronType=Prs', 'PRON', '', ''],
    ['PP__Gender=Masc|Number=Sing|Poss=Yes|PronType=Prs', 'PRON', '', ''],
    ['PP__Number=Plur|Poss=Yes|PronType=Prs', 'PRON', '', ''],
    ['PP__Number=Sing|Poss=Yes|PronType=Prs', 'PRON', '', ''],

    ['PQ__Gender=Fem|Number=Plur|PronType=Int', 'PRON', '', ''],
    ['PQ__Gender=Fem|Number=Sing|PronType=Int', 'PRON', '', ''],
    ['PQ__Gender=Masc|Number=Plur|PronType=Int', 'PRON', '', ''],
    ['PQ__Gender=Masc|Number=Sing|PronType=Int', 'PRON', '', ''],
    ['PQ__Number=Plur|PronType=Int', 'PRON', '', ''],
    ['PQ__Number=Sing|PronType=Int', 'PRON', '', ''],
    ['PQ__PronType=Int', 'PRON', '', ''],

    ['PR__Gender=Masc|Number=Plur|PronType=Rel', 'PRON', '', ''],
    ['PR__Gender=Masc|Number=Sing|PronType=Rel', 'PRON', '', ''],
    ['PR__Gender=Masc|PronType=Rel', 'PRON', '', ''],
    ['PR__Number=Plur|PronType=Rel', 'PRON', '', ''],
    ['PR__Number=Sing|PronType=Rel', 'PRON', '', ''],
    ['PR__Person=3|PronType=Rel', 'PRON', '', ''],
    ['PR__PronType=Rel', 'PRON', '', ''],

    ['RD__Definite=Def', 'DET', '', ''],
    ['RD__Definite=Def|Gender=Fem', 'DET', '', ''],
    ['RD__Definite=Def|Gender=Fem|Number=Plur|PronType=Art', 'DET', '', ''],
    ['RD__Definite=Def|Gender=Fem|Number=Sing|PronType=Art', 'DET', '', ''],
    ['RD__Definite=Def|Gender=Masc|Number=Plur|PronType=Art', 'DET', '', ''],
    ['RD__Definite=Def|Gender=Masc|Number=Sing|PronType=Art', 'DET', '', ''],
    ['RD__Definite=Def|Number=Plur|PronType=Art', 'DET', '', ''],
    ['RD__Definite=Def|Number=Sing|PronType=Art', 'DET', '', ''],
    ['RD__Definite=Def|PronType=Art', 'DET', '', ''],
    ['RD__Gender=Fem|Number=Sing', 'DET', '', ''],
    ['RD__Gender=Masc|Number=Sing', 'DET', '', ''],
    ['RD__Number=Sing', 'DET', '', ''],
    ['RD__Number=Sing|PronType=Art', 'DET', '', ''],

    ['RI__Definite=Ind|Gender=Fem|Number=Plur|PronType=Art', 'DET', '', ''],
    ['RI__Definite=Ind|Gender=Fem|Number=Sing|PronType=Art', 'DET', '', ''],
    ['RI__Definite=Ind|Gender=Masc|Number=Plur|PronType=Art', 'DET', '', ''],
    ['RI__Definite=Ind|Gender=Masc|Number=Sing|PronType=Art', 'DET', '', ''],
    ['RI__Definite=Ind|Number=Sing|PronType=Art', 'DET', '', ''],
    ['RI__Definite=Ind|PronType=Art', 'DET', '', ''],

    ['SP__Gender=Fem|Number=Plur', 'PROPN', '', ''],
    ['SP__NumType=Card', 'PROPN', '', ''],
    ['SP___', 'PROPN', '', ''],

    ['SW__Foreign=Yes', 'X', '', ''],
    ['SW__Foreign=Yes|Gender=Masc', 'X', '', ''],
    ['SW__Foreign=Yes|Number=Sing', 'X', '', ''],

    ['SYM___', 'SYM', '', ''],

    ['S__Gender=Fem', 'NOUN', '', ''],
    ['S__Gender=Fem|Number=Plur', 'NOUN', '', ''],
    ['S__Gender=Fem|Number=Sing', 'NOUN', '', ''],
    ['S__Gender=Masc', 'NOUN', '', ''],
    ['S__Gender=Masc|Number=Plur', 'NOUN', '', ''],
    ['S__Gender=Masc|Number=Sing', 'NOUN', '', ''],
    ['S__Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part', 'NOUN', '', ''],
    ['S__Number=Plur', 'NOUN', '', ''],
    ['S__Number=Sing', 'NOUN', '', ''],
    ['S___', 'NOUN', '', ''],

    ['Sw___', 'X', '', ''],

    ['T__Gender=Fem|Number=Plur|PronType=Tot', 'DET', '', ''],
    ['T__Gender=Fem|Number=Sing', 'DET', '', ''],
    ['T__Gender=Fem|Number=Sing|PronType=Tot', 'DET', '', ''],
    ['T__Gender=Masc|Number=Plur|PronType=Tot', 'DET', '', ''],
    ['T__Gender=Masc|Number=Sing|PronType=Tot', 'DET', '', ''],
    ['T__Number=Plur|PronType=Tot', 'DET', '', ''],
    ['T__PronType=Tot', 'DET', '', ''],

    ['VA__Gender=Fem|Number=Plur|Tense=Past|VerbForm=Part', 'AUX', '', ''],
    ['VA__Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part', 'AUX', '', ''],
    ['VA__Gender=Masc|Number=Plur|Tense=Past|VerbForm=Part', 'AUX', '', ''],
    ['VA__Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part', 'AUX', '', ''],
    ['VA__Mood=Cnd|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VA__Mood=Cnd|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VA__Mood=Cnd|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VA__Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VA__Mood=Ind|Number=Plur|Person=1|Tense=Fut|VerbForm=Fin', 'AUX', '', ''],
    ['VA__Mood=Ind|Number=Plur|Person=1|Tense=Imp|VerbForm=Fin', 'AUX', '', ''],
    ['VA__Mood=Ind|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VA__Mood=Ind|Number=Plur|Person=2|Tense=Fut|VerbForm=Fin', 'AUX', '', ''],
    ['VA__Mood=Ind|Number=Plur|Person=2|Tense=Imp|VerbForm=Fin', 'AUX', '', ''],
    ['VA__Mood=Ind|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VA__Mood=Ind|Number=Plur|Person=3|Tense=Fut|VerbForm=Fin', 'AUX', '', ''],
    ['VA__Mood=Ind|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin', 'AUX', '', ''],
    ['VA__Mood=Ind|Number=Plur|Person=3|Tense=Past|VerbForm=Fin', 'AUX', '', ''],
    ['VA__Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VA__Mood=Ind|Number=Sing|Person=1|Tense=Fut|VerbForm=Fin', 'AUX', '', ''],
    ['VA__Mood=Ind|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin', 'AUX', '', ''],
    ['VA__Mood=Ind|Number=Sing|Person=1|Tense=Past|VerbForm=Fin', 'AUX', '', ''],
    ['VA__Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VA__Mood=Ind|Number=Sing|Person=2|Tense=Fut|VerbForm=Fin', 'AUX', '', ''],
    ['VA__Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VA__Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin', 'AUX', '', ''],
    ['VA__Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin', 'AUX', '', ''],
    ['VA__Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin', 'AUX', '', ''],
    ['VA__Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VA__Mood=Sub|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VA__Mood=Sub|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin', 'AUX', '', ''],
    ['VA__Mood=Sub|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VA__Mood=Sub|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin', 'AUX', '', ''],
    ['VA__Mood=Sub|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin', 'AUX', '', ''],
    ['VA__Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VA__VerbForm=Ger', 'AUX', '', ''],
    ['VA__VerbForm=Inf', 'AUX', '', ''],

    ['VM__Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part', 'AUX', '', ''],
    ['VM__Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part', 'AUX', '', ''],
    ['VM__Mood=Cnd|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Cnd|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Cnd|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Cnd|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Cnd|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Imp|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Imp|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Ind|Number=Plur|Person=1|Tense=Fut|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Ind|Number=Plur|Person=1|Tense=Imp|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Ind|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Ind|Number=Plur|Person=2|Tense=Fut|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Ind|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Ind|Number=Plur|Person=3|Tense=Fut|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Ind|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Ind|Number=Plur|Person=3|Tense=Past|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Ind|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Ind|Number=Sing|Person=2|Tense=Fut|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Ind|Number=Sing|Person=2|Tense=Imp|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Sub|Number=Plur|Person=1|Tense=Imp|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Sub|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Sub|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Sub|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Sub|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin', 'AUX', '', ''],
    ['VM__Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin', 'AUX', '', ''],
    ['VM__VerbForm=Ger', 'AUX', '', ''],
    ['VM__VerbForm=Inf', 'AUX', '', ''],
    
    ['V__Gender=Fem|Number=Plur|Tense=Past|VerbForm=Part', 'VERB', '', ''],
    ['V__Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part', 'VERB', '', ''],
    ['V__Gender=Masc|Number=Plur|Tense=Past|VerbForm=Fin', 'VERB', '', ''],
    ['V__Gender=Masc|Number=Plur|Tense=Past|VerbForm=Part', 'VERB', '', ''],
    ['V__Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part', 'VERB', '', ''],
    ['V__Mood=Cnd|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Cnd|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Cnd|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Cnd|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Cnd|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Imp|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Imp|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Imp|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Imp|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Ind|Number=Plur|Person=1|Tense=Fut|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Ind|Number=Plur|Person=1|Tense=Imp|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Ind|Number=Plur|Person=1|Tense=Past|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Ind|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Ind|Number=Plur|Person=2|Tense=Fut|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Ind|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Ind|Number=Plur|Person=3|Tense=Fut|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Ind|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Ind|Number=Plur|Person=3|Tense=Past|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Ind|Number=Sing|Person=1|Tense=Fut|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Ind|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Ind|Number=Sing|Person=1|Tense=Past|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Ind|Number=Sing|Person=2|Tense=Fut|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Ind|Person=3|Tense=Pres|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Ind|Tense=Pres|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Sub|Number=Plur|Person=1|Tense=Imp|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Sub|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Sub|Number=Plur|Person=2|Tense=Imp|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Sub|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Sub|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Sub|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Sub|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Sub|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Sub|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Sub|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin', 'VERB', '', ''],
    ['V__Mood=Sub|Number=Sing|Person=3|VerbForm=Fin', 'VERB', '', ''],
    ['V__Number=Plur|Tense=Pres|VerbForm=Part', 'VERB', '', ''],
    ['V__Number=Sing|Tense=Pres|VerbForm=Part', 'VERB', '', ''],
    ['V__Tense=Past|VerbForm=Part', 'VERB', '', ''],
    ['V__VerbForm=Ger', 'VERB', '', ''],
    ['V__VerbForm=Inf', 'VERB', '', ''],

    ['_SP', 'X', '', ''],
    ['X___', 'X', '', '']
]
