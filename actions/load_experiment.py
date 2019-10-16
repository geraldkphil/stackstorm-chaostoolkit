#!/usr/bin/env python
from chaoslib.loader import load_experiment
from st2common.runners.base_action import Action
import six


class LoadExperiment(Action):

    def run(self, path):
        experiment = load_experiment(path)
        return experiment