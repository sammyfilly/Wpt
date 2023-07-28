from string import Template
import os
import sys

template = Template("""<!DOCTYPE html>
<!-- This file is generated by $generator -->
<html>
  <head>
    <title>SVG sizing: &lt;$placeholder></title>
    <meta name=timeout content=long>
    <script src="/resources/testharness.js"></script>
    <script src="/resources/testharnessreport.js"></script>
    <script src="../resources/svg-sizing.js"></script>
    <style>
      #testContainer {
          position: absolute;
          left: 0;
          top: 0;
          width: 800px;
          height: 600px
      }
      iframe { border: 0 }
    </style>
    <link rel="help" href="http://www.w3.org/TR/CSS2/visudet.html#inline-replaced-width">
    <link rel="help" href="http://www.w3.org/TR/CSS2/visudet.html#inline-replaced-height">
    <link rel="help" href="https://html.spec.whatwg.org/multipage/#replaced-elements">
    <link rel="help" href="https://html.spec.whatwg.org/multipage/#attr-dim-width">
    <link rel="help" href="http://www.w3.org/TR/SVG/coords.html#ViewportSpace">
  </head>
  <body>
    <div id="log"></div>
    <div id="testContainer"></div>
    <div id="demo"></div>
    <script src="svg-embedded-sizing.js"></script>
    <script>testPlaceholderWithHeight("$placeholder", $placeholderHeightAttr)</script>
  </body>
</html>
""")

placeholders = [ "object", "iframe", "img" ]
placeholderHeightAttrs = [ "null", "'100px'", "'100%'" ]
placeholderHeightAttrsDescriptions = [ "auto", "fixed", "percentage" ]

try:
    os.makedirs("../svg-embedded-sizing")
except OSError:
    pass

for placeholder in placeholders:
    for i, placeholderHeightAttr in enumerate(placeholderHeightAttrs):
        testContent = template.substitute(placeholder=placeholder, placeholderHeightAttr=placeholderHeightAttr, generator=sys.argv[0])
        filename = f"../svg-embedded-sizing/svg-in-{placeholder}-{placeholderHeightAttrsDescriptions[i]}.html"
        with open(filename, "w") as f:
            f.write(testContent)
