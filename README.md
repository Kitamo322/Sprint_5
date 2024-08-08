# <h><center>YANDEX PRACTICUM SPRINT #5<center></h>

<hr>

## Developer: Ivan Generalov

## <h>Cohort: #12</h>
## <h>Project: STELLAR BURGERS</h>
<hr>

## <h>TEST RUN INSTRUCTION:</h>
### <h> -Install pytest by command in terminal: pip install pytest</h>
### <h> -Install selenium by command in terminal: pip install selenium</h>
### <h> -To run all tests use: pytest -v</h>

<hr>

<h3 align="left" style="color:green">Project files and description:</h3>

| File name                    | File Content                                |
|------------------------------|---------------------------------------------|
| test_login.py                | Login tests                                 |
| test_registration.py         | Registration tests                          |
| tests_go_to_personal_area.py | Transfer to personal area tests             |
| test_go_to_constructor.py    | Transfer to constructor area tests          |
| test_exit_button.py          | Logout tests                                |
| test_constructor_area.py     | Swithing between constructor sections tests |
| conftest.py                  | Project system file                         |
| data.py                      | Project data file                           |
| locators.py                  | Project locators file                       |
| generators.py                | Random user generators                      |

<hr>
<h3 align="left" style="color:green">test_login.py</h3>

1. test_login_by_login_button_on_main:

> login test from "login button" on main page

2. test_login_from_personal_area

> login test from "personal area button"

3. test_login_from_registration_area

> login test from "login button" in registration page

4. test_login_from_password_recovery_area

> login test from "login button" in password recovery page
<hr>
<h3 align="left" style="color:green">test_registration.py</h3>

1. test_successful_registration

> new user registration with using personal data random generatos

2. test_registration_error_text

> incorrect error messege text during new user registration
<hr>
<h3 align="left" style="color:green">test_go_to_personal_area.py</h3>

1. test_go_to_personal_area_successful

> successful switch to personal area by click on "personal area button"
<hr>
<h3 align="left" style="color:green">test_go_to_constructor.py</h3>

1. test_go_to_constructor_by_button

> successful switch to constructor area by click on "constructor button" on website hat

2. test_go_to_constructor_by_logo

> successful switch to constructor area by click on "STELLAR BURGERS LOGO" on website hat
<hr>
<h3 align="left" style="color:green">test_constructor_area.py</h3>

1. test_switch_to_buns_section

> successful switch to "BUNS" section by clicking on "BUNS BUTTON"

2. test_switch_to_sauce_section

> successful switch to "SAUCE" section by clicking on "SAUCE BUTTON"

3. test_switch_to_fillers_section

> successful switch to "FILLERS" section by clicking on "FILLERS BUTTON"

<h3 align="left" style="color:green">test_exit_button.py </h3>

1. test_exit_from_personal_area_successful

> successful logout from account by using "Exit" button in personal area






