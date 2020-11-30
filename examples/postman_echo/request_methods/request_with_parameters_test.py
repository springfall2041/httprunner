# NOTE: Generated By HttpRunner v0.0.1
# FROM: request_methods\request_with_parameters.yml


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseRequestWithParameters(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "user_agent": ["iOS/10.1", "iOS/10.2"],
                "username-password": "${parameterize(request_methods/account.csv)}",
                "app_version": "${get_app_version()}",
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = (
        Config("request methods testcase: validate with parameters")
        .variables(**{"app_version": "f1"})
        .base_url("https://postman-echo.com")
        .verify(False)
    )

    teststeps = [
        Step(
            RunRequest("get with params")
            .with_variables(
                **{
                    "foo1": "$username",
                    "foo2": "$password",
                    "sum_v": "${sum_two(1, $app_version)}",
                }
            )
            .get("/get")
            .with_params(**{"foo1": "$foo1", "foo2": "$foo2", "sum_v": "$sum_v"})
            .with_headers(**{"User-Agent": "$user_agent,$app_version"})
            .extract()
            .with_jmespath("body.args.foo2", "session_foo2")
            .validate()
            .assert_equal("status_code", 200)
            .assert_string_equals("body.args.sum_v", "${sum_two(1, $app_version)}")
        ),
    ]


if __name__ == "__main__":
    TestCaseRequestWithParameters().test_start()
