The project repository.

### Clone the Repository:
```bash
git clone https://github.com/pcs-automation-class/linkmygear-test.git
cd linkmygear-test
```

### Create a Virtual Environment:
#### Mac/Linux
 create venv
``` bash
cd [your-repository-folder]
python3 -m venv .venv
```
activate venv
``` bash
source .venv/bin/activate
```
deactivate venv
``` bash
deactivate
```

#### Windows
create venv
``` bash
cd [your-repository-folder]
python3 -m venv .venv
```
activate venv
``` bash
.venv\Scripts\activate
```
deactivate venv
``` bash
deactivate
```


### Install Dependencies:
``` bash
pip install -r requirements.txt
```

### Other
#### list of installed packages
``` bash
pip list
```

#### Which python in use
``` bash
which python    # On Linux/macOS
where python    # On Windows
```

#### Which venv activated
``` bash
echo $VIRTUAL_ENV    # On Linux/macOS
echo %VIRTUAL_ENV%    # On Windows
```

#### Run feature by tags
```gherkin
@smoke
Scenario: Verify the home page title
    Given I open the URL "https://www.google.com"
    Then I verify the title of the page is "Google"
  
@regression
Scenario: Verify the home page title
    Given I open the URL "https://www.google.com"
    Then I verify the title of the page is "Google"

@smoke @regression
Scenario: Verify the home page title
    Given I open the URL "https://www.google.com"
    Then I verify the title of the page is "Google"
 ```
Run the feature file with the tag name
``` bash
behave --tags=@smoke  # Run the feature file with the tag name
behave --tags=@regression --tags=@smoke  # Run the feature file with the tags name
behave --tags=~@smoke  # Run the feature file without the tag name
```


