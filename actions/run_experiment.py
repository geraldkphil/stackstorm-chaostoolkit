#!/usr/bin/env python
from chaoslib.experiment import run_experiment
from st2common.runners.base_action import Action
import six
import chaoslib

class LoadExperiment(Action):

    def run(self, experiment):
        journal = run_experiment(experiment)
        return journal