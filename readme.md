# AWS Edge API Gateway with Key identification

AWS API Gateway provides mechanism to identify source invocation by Key.

This identification is useful to define different usage plans

This project presents a complete way to build an API Gateway with Key identification

## Prerequisites
The CloudFormation template provided by this project require a *Custom Domain Name* as parameter

This *Custom Domain Name* (usually something like *api.mycompany.com*) is better to be configured as *Edge optimized* to avoid issues with [private API](https://github.com/cannereau/api-private)


## Build the API Gateway
The tricky part of the template is the association between the **API Rest**, the **Key** and the **Plan** :

        HelloApiKey:
          Type: "AWS::ApiGateway::ApiKey"
          DependsOn: HelloApiStage
          Properties:
            Name: "hello-key"
            Description: "Hello API Key"
            Enabled: "true"
            StageKeys:
            -
              RestApiId: !Ref HelloApiGateway
              StageName: "prod"

        HelloApiPlan:
          Type: "AWS::ApiGateway::UsagePlan"
          Properties:
            UsagePlanName: "hello-plan"
            Description: "Plan to say Hello"
            Quota:
              Limit: 1000
              Period: "DAY"
            Throttle:
              RateLimit: 100
              BurstLimit: 200
            ApiStages:
            - ApiId: !Ref HelloApiGateway
              Stage: "prod"

        HelloApiPlanKey:
          Type: "AWS::ApiGateway::UsagePlanKey"
          Properties : 
            KeyId: !Ref HelloApiKey
            KeyType: "API_KEY"
            UsagePlanId: !Ref HelloApiPlan

## Usage
To make a identified request on this API Gateway, just add a header named "*x-api-key*" with the "*Key Value*" as value
