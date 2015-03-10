# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# This is a plotting script to display average relative differences of 42
# scenarios.
#
# ------------------------------------------------------------------------------

# File:         plot_meanstd.py
# Author:       Hongwei Jin
# Created:      03/09/2015

import matplotlib.pyplot as plt
import os


def main():
    mean = [0.82030573545225283, 0.45143062768248321, 0.59798725660521046, 0.76437323433166215, 0.78990414803181441, 0.64674171232803079, 0.79174122556310367, 0.88647129304872074, 0.77211212830955311, 0, 0.8902211407039391, 0.84144780402445063, 0.82628631489337967, 0.85622751796827146, 0.7024057452251401, 0.88137567112370563, 0.89609661782053918, 0.88320411766355, 0.77203204181346075, 0.78051027741334278,
            0.81666251432056447, 0.81523885748131963, 0.74646766036314649, 0, 0.81862475366271836, 0.62685474586031187, 0.76469054316357365, 0.49432195202882562, 0, 0.78183192751116248, 0.78922354409656537, 0.94493658188569685, 0.5284400889429115, 0.89642087979464868, 0.43538793402087128, 0.83329075999600499, 0.84099375691772937, 0.74528045193524184, 0.74219519588941829, 0, 0.76608203123467222, 0.10139755585616865]
    std = [0.15938360580881983, 0.23642837069013828, 0.22754575206893143, 0.18431731649915009, 0.16025238694812272, 0.20923203409335739, 0.11280114985770098, 0.072644268244583615, 0.17183219856805784, 0, 0.0077713942265878275, 0.088626776918447697, 0.13585043576415973, 0.080382066539769231, 0.24215661278132317, 0.076571149315857345, 0.052355173396202381, 0.0, 0.17405695669218868,
           0.15653159298279851, 0.13812190860818016, 0.13663200895440433, 0.18726985597997167, 0, 0.15627613808241766, 0.19764524111829554, 0.16615992157511317, 0.2285599635544131, 0, 0.15322657185557714, 0.14254606066576567, 0.0, 0.22512187626273242, 0.044215765473707862, 0.0, 0.11002093412077706, 0.11241710548806295, 0.2060535536984513, 0.18193084028437326, 0, 0.17891823729079437, 0.0]
    labels = ['s{}'.format(i) for i in range(len(mean))]
    plt.errorbar(mean, len(mean) * [0], std, linestyle='None', marker="x")
    plt.title('Ava. Re. Dif. of 42 Scenarios')
    plt.xlabel('Avg. Relative Difference')
    plt.savefig(os.path.join(CURRENT_FOLDER, "..\\Figures\\means.png"))

if __name__ == '__main__':
    CURRENT_FOLDER = os.path.dirname(os.path.realpath(__file__))
    main()