# Amazon CodeWhisperer Customization Demo

This is a demo for Amazon CodeWhisperer's Customization feature. In this example we work for Acme Corp, who has created a strategic differentiation by aligning value streams across industry verticals. We also have a very sercret Python library that is the key to our business success if we can just get the engineers to use it correctly.

Hatchet is used to take logs and make them ready for the cloud by `chop`ing them into smaller pieces. The `chop` method takes two parameters, a `string` that represents the log contents and an `Enum` that indicates the required log level. A sample `chop` looks like this

```python
hatchet.chop('lorem ipsum', Level.INFO)
```

Because this SDK is proprietary and private to our company, traditional Generative AI coding assistants are unable to offer recommendations that include references to `Hatchet`. CodeWhisperer Customizations can address this gap by allowing us to create a custom model that can only be used through our intetnal Identity Provider (IdP).

## Training Repo

This is not the repository that will be used for training, but a tribute to such a repository. Because CodeWhisperer requires >10MB of source files for a customization job, it's more practical to generate the training data when needed than to share the whole trainign set directly.

To generate the training data, deploy the AWS SAM application with the following command

```bash
sam build --use-container
sam deploy --guided --region us-east-1
```

Once the application is done deploying, you will need to 'poke' the Lambda Function to get it to generate the sample data. Before you can invoke it, you will need to retrieve the name of the Lambda Function from the SAM CLI output. The last lines of the CLI output should look similar to the following. Copy the `Value` for the `FunctionName` output to use in the next step.

```
CloudFormation outputs from deployed stack
------------------
Outputs                  
------------------
Key                 FunctionName
Description         Name of the created Lambda Function
Value               cwspr-test-GeneratorFunction-wBPiHGRosnom

------------------
```

```bash
aws lambda invoke \
    --function-name REPLACE_ME_WITH_VALUE \
    --cli-binary-format raw-in-base64-out \
    --payload '{}' \
    --region us-east-1 \
    --cli-read-timeout 930 \
    response.json
```

Once the command completes (should take about 10 minutes to generate the trainign data) you can navigate to the CodeWhisperer Management Console and create a new customization with the location specified in `response.json`.

TODO: add screenshots for creating customization

## Using the Customization
Once the customization has been created and activated it is ready to use. Once you've enabled the customization for a particular SSO User, you can test it by opening your IDE, selecting the customization from the AWS Toolkit for your preferred IDE, and typing the following:

```python
from timber.hatchet import Hatchet
from timber.level import Level
from timber.stage import Stage

# instantiate a hatchet instance
hatchet = Hatchet(endpoint='https://timber.acme.dev', service_name='pumpkin', stage=Stage.Prod)

def my_function():
  x = 50
  # use hatchet to chop logs for x
```
At this point, CodeWhisperer should provide the following suggestion for the next line

```python
  hatchet.chop("x was reassigned", Level.WARN)
```


## Cleanup

TODO: Describe emptying and deleting the bucket

TODO: Deactivate customization

TODO: Delete CloudFormation Template

