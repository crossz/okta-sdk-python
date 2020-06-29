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


from urllib.parse import urlencode


class OAuth2ScopeConsentGrant:
    def __init__(self, config=None):
        if config:
            self.embedded = config["_embedded"]
            self.links = config["_links"]
            self.client_id = config["clientId"]
            self.created = config["created"]
            self.created_by = config["createdBy"]
            self.id = config["id"]
            self.issuer = config["issuer"]
            self.last_updated = config["lastUpdated"]
            self.scope_id = config["scopeId"]
            self.source = config["source"]
            self.status = config["status"]
            self.user_id = config["userId"]
        else:
            self.embedded = None
            self.links = None
            self.client_id = None
            self.created = None
            self.created_by = None
            self.id = None
            self.issuer = None
            self.last_updated = None
            self.scope_id = None
            self.source = None
            self.status = None
            self.user_id = None


# End of File Generation
