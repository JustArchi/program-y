import unittest

from programy.config.client.webchat import WebChatConfiguration
from programy.config.file.yaml import YamlConfigurationFile
from programy.config.client.client import ClientConfiguration
from programy.config.client.webchat import WebChatClientConfiguration


class WebChatConfigurationTests(unittest.TestCase):

    def test_init(self):
        client_config = ClientConfiguration()
        yaml = YamlConfigurationFile(client_config)
        self.assertIsNotNone(yaml)
        yaml.load_from_text("""
        webchat:
          host: 127.0.0.1
          port: 5000
          debug: false
        """, ".")

        webchat_config = WebChatConfiguration()
        webchat_config.load_config_section(yaml, ".")

        self.assertEqual("127.0.0.1", webchat_config.host)
        self.assertEqual(5000, webchat_config.port)
        self.assertEqual(False, webchat_config.debug)


class WebChatClientConfigurationTests(unittest.TestCase):

    def test_init(self):
        client_config = WebChatClientConfiguration()

        yaml = YamlConfigurationFile(client_config)
        self.assertIsNotNone(yaml)
        yaml.load_from_text("""
        brain:
          supress_warnings: true
          allow_system_aiml: true
          allow_learn_aiml: true
          allow_learnf_aiml: true

          files:
              aiml:
                  files: /aiml
                  extension: .aiml
                  directories: true
              sets:
                  files: /sets
                  extension: .txt
                  directories: false
              maps:
                  files: /maps
                  extension: .txt
                  directories: true
              denormal: denormal.txt
              normal: normal.txt
              gender: gender.txt
              person: person.txt
              person2: person2.txt
              predicates: predicates.txt
              pronouns: pronouns.txt
              properties: properties.txt
              triples: triples.txt
              preprocessors: preprocessors.txt
              postprocessors: postprocessors.txt

          services:
              REST:
                  path: programy.utils.services.webchat.GenericRESTService
              Pannous:
                  path: programy.utils.services.pannous.PannousService
              Pandora:
                  path: programy.utils.services.pandora.PandoraService
              Wikipedia:
                  path: programy.utils.services.wikipedia.WikipediaService

        bot:
          prompt: ">>>"
          default_response: Sorry, I don't have an answer for that!
          exit_response: So long, and thanks for the fish!
          initial_question: Hi, how can I help you?

        webchat:
          host: 127.0.0.1
          port: 5000
          debug: false
          """, ".")

        self.assertIsNotNone(client_config.bot_configuration)
        self.assertIsNotNone(client_config.brain_configuration)
        self.assertIsNotNone(client_config.webchat_configuration)
