import unittest
import requests
import responses


class TestAPI(unittest.TestCase):
    @responses.activate  # intercept HTTP calls within this method
    def test_simple(self):
        response_data = {
                "id": "ch_1GH8so2eZvKYlo2CSMeAfRqt",
                "object": "charge",
                "customer": {"id": "cu_1GGwoc2eZvKYlo2CL2m31GRn", "object": "customer"},
            }
        # mock the Stripe API
        responses.add(
            responses.GET,
            "https://api.stripe.com/v1/charges",
            json=response_data,
        )

        response = requests.get("https://api.stripe.com/v1/charges")
        self.assertEqual(response.json(), response_data)