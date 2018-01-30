class BasePruner(object):

    def prune(self, storage, study_id, trial_id, step):
        return NotImplementedError


class MedianPruner(BasePruner):

    """Pruner using median

     Prune if the trial's best intermediate result is worse than
     median of intermediate results of previous trials at the same step.
    """

    def prune(self, storage, study_id, trial_id, step):
        best_intermediate_result = storage.get_best_intermediate_result_over_steps(
            study_id, trial_id)
        median = storage.get_median_intermediate_result_over_trials(
            study_id, step)

        print(step, best_intermediate_result, median)

        return best_intermediate_result > median