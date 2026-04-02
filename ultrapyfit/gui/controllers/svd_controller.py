from PySide6 import QtWidgets


class SVDController:
    def __init__(self, main_window):
        self.mw = main_window

    def update_svd_math(self):
        experiment = self.mw.get_experiment()
        if experiment:
            calc_comps, _, _ = self.get_svd_parameters()
            experiment.calculate_svd(n_components=calc_comps)
            self.mw.plot_controller.plot_current_data_svd()
            self.mw.sldSvdShowComps.setMaximum(self.mw.sbSvdCalcComps.value())
            self.mw.sbSvdShowComps.setMaximum(self.mw.sbSvdCalcComps.value())

    def get_svd_parameters(self):
        calc = self.mw.sbSvdCalcComps.value()
        show = self.mw.sldSvdShowComps.value()
        log = self.mw.chkSvdLogScale.isChecked()
        
        if calc < show:
            calc = show
            self.mw.sbSvdCalcComps.blockSignals(True)
            self.mw.sbSvdCalcComps.setValue(calc)
            self.mw.sbSvdCalcComps.blockSignals(False)
            
        return calc, show, log
