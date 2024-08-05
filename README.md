<h1 align="left" style="color:#FFA500">YANDEX PRACTICUM SPRINT #5</h1>
<hr>
<h3 align="left" style="color:#9E7BFF">Developer: Ivan Generalov</h3>
<h3 align="left" style="color:#9E7BFF">Cohort: #12</h3>
<h3 align="left" style="color:#9E7BFF">Project: STELLAR BURGERS</h3>
<hr>
<h3 align="left" style="color:#E42217">TEST RUN INSTRUCTION:</h3>
<h3 align="left">To run my tests, you must add two system environment variables "MYPASSWORD" and "MYLOGIN". 
You can register an account using this link -> https://stellarburgers.nomoreparties.site/register </h3>
<hr>

<h3 align="left" style="color:green">Project files and description:</h3>

| File name                 | File Content                                |
|---------------------------|---------------------------------------------|
| test_login.py             | Login tests                                 |
| test_registration.py      | Registration tests                          |
| tests_go_to_personal_area | Transfer to personal area tests             |
| test_go_to_constructor    | Transfer to constructor area tests          |
| test_exit_button          | Logout tests                                |
| test_constructor_area.py  | Swithing between constructor sections tests |
| conftest.py               | Project system file                         |
| data.py                   | Project data file                           |
| locators.py               | Project locators file                       |
| generators.py             | Random user generators                      |

<hr>
<h3 align="left" style="color:green">test_login.py</h3>

1. test_login_by_login_button_on_main:

> login test from "login button" on main page
git 
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




