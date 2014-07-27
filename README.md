JSONPML2DOT
===========

Generates a [DOT](http://www.graphviz.org/) file using a BigML [JSON PML](https://github.com/bigmlcom/json-pml) model as input

1. Install bigml:

        pip install bigml

2. Set up your BIGML_USERNAME and BIGML_API_KEY

   [Setting up BigML authentication](https://bigml.com/developers/quick_start#q_authenticate)

        export BIGML_USERNAME=myuser
        export BIGML_API_KEY=5ff31045b4f4582907d90011a5fab240442rc734e
        export BIGML_AUTH="username=$BIGML_USERNAME;api_key=$BIGML_API_KEY"

3. Simple usage

        ./jsonpml2dot --model model/53c4e07b48d9b63686000342 --output mymodel.dot

4. Generating a png

        ./jsonpml2dot --model model/53c4e07b48d9b63686000342 | dot -Tpng > mymodel.png

5. Generating a png from a public model

        ./jsonpml2dot.py --model public/model/53b2f21ec8db635905000d33 | dot -Tpng > heartdisease.png

<img src="https://raw.github.com/aficionado/jsonpml2dot/master/images/heartdisease.png" alt="tree model">
[BigML's compact and interactive represenation](https://bigml.com/user/ashikiar/gallery/model/53b2f21ec8db635905000d33)


6. Generating a png from shared model

        ./jsonpml2dot.py --model shared/model/vZ88ZkoIK2faSqDq7Wod7hFQxe5 | dot -Tpng > credit.png

<img src="https://raw.github.com/aficionado/jsonpml2dot/master/images/credit.png" alt="tree model">
[BigML's compact and interactive represenation](https://bigml.com/shared/model/vZ88ZkoIK2faSqDq7Wod7hFQxe5)



