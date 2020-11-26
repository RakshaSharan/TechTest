Feature: Returns a list of articles

Background:
  Given Set api endpoint as "https://5f99522350d84900163b8737.mockapi.io/tech-test/articles"

@getTag
Scenario: Get list of articles
  When  Raise "GET" HTTP request
  Then Response http code should be 200 for "GET"
  And Response HEADER content type should be "application/json"

@postTag
Scenario: Post list of articles
  When  Raise "POST" HTTP request
  Then Response http code should be 404 for "POST"

@putTag
Scenario: Put list of articles
  When  Raise "PUT" HTTP request
  Then Response http code should be 404 for "PUT"

@deleteTag
Scenario: Delete list of articles
  When  Raise "DELETE" HTTP request
  Then Response http code should be 404 for "DELETE"
