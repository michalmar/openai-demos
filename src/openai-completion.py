import os
import openai
openai.api_type = "azure"
openai.api_base = "https://mma-openai.openai.azure.com/"
openai.api_version = "2022-03-01-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  engine="mma-first-deployment",
  prompt="A neutron star is the collapsed core of a massive supergiant star, which had a total mass of between 10 and 25 solar masses, possibly more if the star was especially metal-rich.[1] Neutron stars are the smallest and densest stellar objects, excluding black holes and hypothetical white holes, quark stars, and strange stars.[2] Neutron stars have a radius on the order of 10 kilometres (6.2 mi) and a mass of about 1.4 solar masses.[3] They result from the supernova explosion of a massive star, combined with gravitational collapse, that compresses the core past white dwarf star density to that of atomic nuclei.\n\n\nTl;dr",
  temperature=0.7,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None
)

text = response['choices'][0]['text'].split('\n')[0]
print(start_phrase+text)

