import pytest
from PP_Automation_Testing.Moduless.Test_Dashboard import Test_Dashboard
from PP_Automation_Testing.Moduless.Test_Pomanagment import Test_Pomangment


@pytest.mark.usefixtures('setup')
class Test_all:
    @pytest.mark.second
    def test_dashboard(self):
        self.obj1=Test_Dashboard(self.driver)
        self.obj1.test_dashboradlanding()

    def test_Pomangment(self):
        self.obj= Test_Pomangment(self.driver)
        self.obj.test_button()
        self.obj.test_include_close_checkbox()
        self.obj.test_create_po()
        self.obj.test_reject_po()



