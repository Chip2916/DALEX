from .._plot_container import PlotContainer

class BreakDownContainer(PlotContainer):
    info = {
        'name': "Break Down",
        'plotType': "Breakdown",
        'plotCategory': "Observation Level",
        'requiredParams': ["model", "observation"]
    }
    options = {
    }
    def _fit(self, model, observation):
        bd = model.explainer.predict_parts(observation.get_row(), type='break_down').result
        self.data = {
            'variables': bd[1:-1].variable_name.tolist(),
            'variables_value': bd[1:-1].variable_value.tolist(),
            'contribution': bd[1:-1].contribution.tolist(),
            'intercept': bd.contribution[0],
            'prediction': bd.cumulative.tail(1).iloc[0]
        }
