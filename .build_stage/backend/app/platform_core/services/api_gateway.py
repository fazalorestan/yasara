class APIGatewayUtilities:
    def standard_response(self, ready=True, **kwargs):
        p={'ready':ready}; p.update(kwargs); return p
api_gateway_utilities=APIGatewayUtilities()
