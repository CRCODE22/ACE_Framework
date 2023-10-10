from ace.framework.layer import Layer, LayerSettings
from ace.framework.prompts.identities import l2_identity


class Layer2(Layer):

    @property
    def settings(self):
        return LayerSettings(
            name="layer_2",
            label="Global Strategy",
        )

    # TODO: Add valid status checks.
    def status(self):
        self.log.debug(f"Checking {self.labeled_name} status")
        return self.return_status(True)

    def set_identity(self):
        self.identity=l2_identity

    def process_layer_messages(self, control_messages, data_messages, request_messages, response_messages, telemetry_messages):
        # Create operation classifier prompt
        # Get operation classification
        # Parse operation classification for SOUTH
        # For each bus direction:
        #   If classification is TAKE_ACTION, select appropriate southbound output message from outputs.py to render operations prompt
        #   Render appropraite operations prompt from operation_descriptions.py
        # Create layer instruction prompt using layer_instructions.py
        # Parse output messages into message types 
        # Return messages
        pass