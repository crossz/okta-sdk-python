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


class Group:
    def __init__(self, config=None):
        if config:
            self.embedded = config["_embedded"]
            self.links = config["_links"]
            self.created = config["created"]
            self.id = config["id"]
            self.last_membership_updated = config["lastMembershipUpdated"]
            self.last_updated = config["lastUpdated"]
            self.object_class = config["objectClass"]
            self.profile = config["profile"]
            self.type = config["type"]
        else:
            self.embedded = None
            self.links = None
            self.created = None
            self.id = None
            self.last_membership_updated = None
            self.last_updated = None
            self.object_class = None
            self.profile = None
            self.type = None

    # Updates the profile for a group with &#x60;OKTA_GROUP&#x60; type from your organization.
    async def update_group(
            self, groupId, group
    ):
        """
            Updates the profile for a group with `OKTA_GROUP` type
        from your organization.
        Args:
            group_id {str}
            {group}
        Returns:
            Group
        """
        http_method = "put".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups/{groupId}
            """)

        body = group
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        try:
            result = Group(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Removes a group with &#x60;OKTA_GROUP&#x60; type from your organization.
    async def delete_group(
            self, groupId
    ):
        """
            Removes a group with `OKTA_GROUP` type from your organi
        zation.
        Args:
            group_id {str}
        """
        http_method = "delete".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups/{groupId}
            """)

        body = None
        headers = None

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        return (response, None)

    # Enumerates groups in your organization with pagination. A subset of groups can be returned that match a supported filter expression or query.
    async def list_groups(
            self, query_params
    ):
        """
            Enumerates groups in your organization with pagination.
        A subset of groups can be returned that match a suppor
        ted filter expression or query.
        Args:
            query_params {dict}: Map of query parameters for request
            [query_params.q] {str}
            [query_params.filter] {str}
            [query_params.after] {str}
            [query_params.limit] {str}
        Returns:
            list: Collection of Group instances.
        """
        http_method = "get".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups
            """)
        encoded_query_params = urlencode(query_params)
        api_url += f"/?{encoded_query_params}"

        body = None
        headers = None

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        try:
        result = []
        for item in response.get_body():
            result.append(Group(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    # Adds a new group with &#x60;OKTA_GROUP&#x60; type to your organization.
    async def create_group(
            self, group
    ):
        """
            Adds a new group with `OKTA_GROUP` type to your organiz
        ation.
        Args:
            {group}
        Returns:
            Group
        """
        http_method = "post".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups
            """)

        body = group
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        try:
            result = Group(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Lists all group rules for your organization.
    async def list_group_rules(
            self, query_params
    ):
        """
            Lists all group rules for your organization.
        Args:
            query_params {dict}: Map of query parameters for request
            [query_params.limit] {str}
            [query_params.after] {str}
            [query_params.search] {str}
            [query_params.expand] {str}
        Returns:
            list: Collection of GroupRule instances.
        """
        http_method = "get".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups/rules
            """)
        encoded_query_params = urlencode(query_params)
        api_url += f"/?{encoded_query_params}"

        body = None
        headers = None

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        try:
        result = []
        for item in response.get_body():
            result.append(GroupRule(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    # Creates a group rule to dynamically add users to the specified group if they match the condition
    async def create_group_rule(
            self, group_rule
    ):
        """
            Creates a group rule to dynamically add users to the sp
        ecified group if they match the condition
        Args:
            {group_rule}
        Returns:
            GroupRule
        """
        http_method = "post".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups/rules
            """)

        body = group_rule
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        try:
            result = GroupRule(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Removes a specific group rule by id from your organization
    async def delete_group_rule(
            self, ruleId
    ):
        """
            Removes a specific group rule by id from your organizat
        ion
        Args:
            rule_id {str}
        """
        http_method = "delete".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups/rules/{ruleId}
            """)

        body = None
        headers = None

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        return (response, None)

    # Fetches a specific group rule by id from your organization
    async def get_group_rule(
            self, ruleId, query_params
    ):
        """
            Fetches a specific group rule by id from your organizat
        ion
        Args:
            rule_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.expand] {str}
        Returns:
            GroupRule
        """
        http_method = "get".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups/rules/{ruleId}
            """)
        encoded_query_params = urlencode(query_params)
        api_url += f"/?{encoded_query_params}"

        body = None
        headers = None

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        try:
            result = GroupRule(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Updates a group rule. Only &#x60;INACTIVE&#x60; rules can be updated.
    async def update_group_rule(
            self, ruleId, group_rule
    ):
        """
            Updates a group rule. Only `INACTIVE` rules can be upda
        ted.
        Args:
            rule_id {str}
            {group_rule}
        Returns:
            GroupRule
        """
        http_method = "put".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups/rules/{ruleId}
            """)

        body = group_rule
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        try:
            result = GroupRule(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Activates a specific group rule by id from your organization
    async def activate_group_rule(
            self, ruleId
    ):
        """
            Activates a specific group rule by id from your organiz
        ation
        Args:
            rule_id {str}
        """
        http_method = "post".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups/rules/{ruleId}/lifecycle/activate
            """)

        body = None
        headers = None

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        return (response, None)

    # Deactivates a specific group rule by id from your organization
    async def deactivate_group_rule(
            self, ruleId
    ):
        """
            Deactivates a specific group rule by id from your organ
        ization
        Args:
            rule_id {str}
        """
        http_method = "post".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups/rules/{ruleId}/lifecycle/deactivate
            """)

        body = None
        headers = None

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        return (response, None)

    # Lists all group rules for your organization.
    async def get_group(
            self, groupId
    ):
        """
            Lists all group rules for your organization.
        Args:
            group_id {str}
        Returns:
            Group
        """
        http_method = "get".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups/{groupId}
            """)

        body = None
        headers = None

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        try:
            result = Group(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Enumerates all applications that are assigned to a group.
    async def list_assigned_applications_for_group(
            self, groupId, query_params
    ):
        """
            Enumerates all applications that are assigned to a grou
        p.
        Args:
            group_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.after] {str}
            [query_params.limit] {str}
        Returns:
            list: Collection of Application instances.
        """
        http_method = "get".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups/{groupId}/apps
            """)
        encoded_query_params = urlencode(query_params)
        api_url += f"/?{encoded_query_params}"

        body = None
        headers = None

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        try:
        result = []
        for item in response.get_body():
            result.append(Application(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    
    async def list_group_assigned_roles(
            self, groupId, query_params
    ):
        """
            Success
        Args:
            group_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.expand] {str}
        Returns:
            list: Collection of Role instances.
        """
        http_method = "get".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups/{groupId}/roles
            """)
        encoded_query_params = urlencode(query_params)
        api_url += f"/?{encoded_query_params}"

        body = None
        headers = None

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        try:
        result = []
        for item in response.get_body():
            result.append(Role(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    # Assigns a Role to a Group
    async def assign_role_to_group(
            self, groupId, assign_role_request, query_params
    ):
        """
            Assigns a Role to a Group
        Args:
            group_id {str}
            {assign_role_request}
            query_params {dict}: Map of query parameters for request
            [query_params.disableNotifications] {str}
        Returns:
            Role
        """
        http_method = "post".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups/{groupId}/roles
            """)
        encoded_query_params = urlencode(query_params)
        api_url += f"/?{encoded_query_params}"

        body = assign_role_request
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        try:
            result = Role(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Unassigns a Role from a Group
    async def remove_role_from_group(
            self, groupId, roleId
    ):
        """
            Unassigns a Role from a Group
        Args:
            group_id {str}
            role_id {str}
        """
        http_method = "delete".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups/{groupId}/roles/{roleId}
            """)

        body = None
        headers = None

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        return (response, None)

    
    async def get_role(
            self, groupId, roleId
    ):
        """
            Success
        Args:
            group_id {str}
            role_id {str}
        Returns:
            Role
        """
        http_method = "get".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups/{groupId}/roles/{roleId}
            """)

        body = None
        headers = None

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        try:
            result = Role(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Lists all App targets for an &#x60;APP_ADMIN&#x60; Role assigned to a Group. This methods return list may include full Applications or Instances. The response for an instance will have an &#x60;ID&#x60; value, while Application will not have an ID.
    async def list_app_targets_for_application_admin_role_for_group(
            self, groupId, roleId, query_params
    ):
        """
            Lists all App targets for an `APP_ADMIN` Role assigned
        to a Group. This methods return list may include full A
        pplications or Instances. The response for an instance
        will have an `ID` value, while Application will not hav
        e an ID.
        Args:
            group_id {str}
            role_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.after] {str}
            [query_params.limit] {str}
        Returns:
            list: Collection of CatalogApplication instances.
        """
        http_method = "get".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups/{groupId}/roles/{roleId}/targets
                catalog/apps
            """)
        encoded_query_params = urlencode(query_params)
        api_url += f"/?{encoded_query_params}"

        body = None
        headers = None

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        try:
        result = []
        for item in response.get_body():
            result.append(CatalogApplication(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    
    async def remove_app_target_from_application_admin_role_given_to_group(
            self, groupId, roleId, appName
    ):
        """
            Success
        Args:
            group_id {str}
            role_id {str}
            app_name {str}
        """
        http_method = "delete".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups/{groupId}/roles/{roleId}/targets
                catalog/apps/{appName}
            """)

        body = None
        headers = None

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        return (response, None)

    
    async def add_application_target_to_admin_role_given_to_group(
            self, groupId, roleId, appName
    ):
        """
            Success
        Args:
            group_id {str}
            role_id {str}
            app_name {str}
        """
        http_method = "put".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups/{groupId}/roles/{roleId}/targets
                catalog/apps/{appName}
            """)

        body = None
        headers = None

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        return (response, None)

    # Remove App Instance Target to App Administrator Role given to a Group
    async def remove_app_target_from_admin_role_given_to_group(
            self, groupId, roleId, appName, applicationId
    ):
        """
            Remove App Instance Target to App Administrator Role gi
        ven to a Group
        Args:
            group_id {str}
            role_id {str}
            app_name {str}
            application_id {str}
        """
        http_method = "delete".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups/{groupId}/roles/{roleId}/targets
                catalog/apps/{appName}/{applicationId}
            """)

        body = None
        headers = None

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        return (response, None)

    # Add App Instance Target to App Administrator Role given to a Group
    async def add_app_instance_target_to_app_admin_role_given_to_group(
            self, groupId, roleId, appName, applicationId
    ):
        """
            Add App Instance Target to App Administrator Role given
        to a Group
        Args:
            group_id {str}
            role_id {str}
            app_name {str}
            application_id {str}
        """
        http_method = "put".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups/{groupId}/roles/{roleId}/targets
                catalog/apps/{appName}/{applicationId}
            """)

        body = None
        headers = None

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        return (response, None)

    
    async def list_group_targets_for_group_role(
            self, groupId, roleId, query_params
    ):
        """
            Success
        Args:
            group_id {str}
            role_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.after] {str}
            [query_params.limit] {str}
        Returns:
            list: Collection of Group instances.
        """
        http_method = "get".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups/{groupId}/roles/{roleId}/targets
                groups
            """)
        encoded_query_params = urlencode(query_params)
        api_url += f"/?{encoded_query_params}"

        body = None
        headers = None

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        try:
        result = []
        for item in response.get_body():
            result.append(Group(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    # 
    async def remove_group_target_from_group_admin_role_given_to_group(
            self, groupId, roleId, targetGroupId
    ):
        """
            Method for
        /api/v1/groups/{groupId}/roles/{roleId}/targets/groups/
        {targetGroupId}
        Args:
            group_id {str}
            role_id {str}
            target_group_id {str}
        """
        http_method = "delete".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups/{groupId}/roles/{roleId}/targets
                groups/{targetGroupId}
            """)

        body = None
        headers = None

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        return (response, None)

    # 
    async def add_group_target_to_group_administrator_role_for_group(
            self, groupId, roleId, targetGroupId
    ):
        """
            Method for
        /api/v1/groups/{groupId}/roles/{roleId}/targets/groups/
        {targetGroupId}
        Args:
            group_id {str}
            role_id {str}
            target_group_id {str}
        """
        http_method = "put".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups/{groupId}/roles/{roleId}/targets
                groups/{targetGroupId}
            """)

        body = None
        headers = None

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        return (response, None)

    # Enumerates all users that are a member of a group.
    async def list_group_users(
            self, groupId, query_params
    ):
        """
            Enumerates all users that are a member of a group.
        Args:
            group_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.after] {str}
            [query_params.limit] {str}
        Returns:
            list: Collection of User instances.
        """
        http_method = "get".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups/{groupId}/users
            """)
        encoded_query_params = urlencode(query_params)
        api_url += f"/?{encoded_query_params}"

        body = None
        headers = None

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        try:
        result = []
        for item in response.get_body():
            result.append(User(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    # Removes a user from a group with &#x27;OKTA_GROUP&#x27; type.
    async def remove_user_from_group(
            self, groupId, userId
    ):
        """
            Removes a user from a group with 'OKTA_GROUP' type.
        Args:
            group_id {str}
            user_id {str}
        """
        http_method = "delete".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups/{groupId}/users/{userId}
            """)

        body = None
        headers = None

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        return (response, None)

    # Adds a user to a group with &#x27;OKTA_GROUP&#x27; type.
    async def add_user_to_group(
            self, groupId, userId
    ):
        """
            Adds a user to a group with 'OKTA_GROUP' type.
        Args:
            group_id {str}
            user_id {str}
        """
        http_method = "put".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups/{groupId}/users/{userId}
            """)

        body = None
        headers = None

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        return (response, None)


# End of File Generation
