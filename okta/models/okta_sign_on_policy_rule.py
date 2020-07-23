"""
Copyright 2020 - Present Okta, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# AUTO-GENERATED! DO NOT EDIT FILE DIRECTLY
# SEE CONTRIBUTOR DOCUMENTATION

from okta.models.policy_rule\
    import PolicyRule
from okta.models.okta_sign_on_policy_rule_actions\
    import OktaSignOnPolicyRuleActions
from okta.models.okta_sign_on_policy_rule_conditions\
    import OktaSignOnPolicyRuleConditions


class OktaSignOnPolicyRule(
    PolicyRule
):
    """
    A class for OktaSignOnPolicyRule objects.
    """

    def __init__(self, config=None):
        if config:
            if "actions" in config:
                if isinstance(config["actions"],
                              OktaSignOnPolicyRuleActions):
                    self.actions = config["actions"]
                else:
                    self.actions = OktaSignOnPolicyRuleActions(
                        config["actions"]
                    )
            else:
                self.actions = None
            if "conditions" in config:
                if isinstance(config["conditions"],
                              OktaSignOnPolicyRuleConditions):
                    self.conditions = config["conditions"]
                else:
                    self.conditions = OktaSignOnPolicyRuleConditions(
                        config["conditions"]
                    )
            else:
                self.conditions = None
            self.name = config["name"]\
                if "name" in config else None
        else:
            self.actions = None
            self.conditions = None
            self.name = None

    def request_format(self):
        return {
            "actions": self.actions,
            "conditions": self.conditions,
            "name": self.name
        }
