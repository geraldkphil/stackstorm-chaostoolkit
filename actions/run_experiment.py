#!/usr/bin/env python
from chaoslib.experiment import run_experiment
from chaoslib.loader import load_experiment
from st2common.runners.base_action import Action


class RunExperiment(Action):

    def run(self, path):
        experiment = load_experiment(path)
        journal = run_experiment(experiment)
        return journal
