Feature: Returns a single article

Background:
  Given Set GET api endpoint as "https://5f99522350d84900163b8737.mockapi.io/tech-test/articles/2"

@getTag1
Scenario: Get a single article
  When  Raise "GET" HTTP request
  Then Response http code should be 200 for "GET"
  And Response HEADER content type should be "application/json"

@postTag1
Scenario: Post a single article
  When  Raise "POST" HTTP request
  Then Response http code should be 404 for "POST"

@putTag1
Scenario: Put a single article
  When  Raise "PUT" HTTP request
  Then Response http code should be 404 for "PUT"

@deleteTag1
Scenario: Delete a single article
  When  Raise "DELETE" HTTP request
  Then Response http code should be 404 for "DELETE"