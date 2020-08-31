# Setur.com.tr Front End Test Automation Python-Selenium
## This documentation contains critical information about the test automation and suggestions about how to proceed the roadmap and program.

### How could we make the development process better?

  Having a development can be thought as a tree that has multiple sides. First, the product management team would have a vision. They would do the marketing research to make their vision become as real as possible within the best features compared to the product on the market to make it as compatible as possible. Once they grow their vision, they prepare a documentation for making the transmission completed to the rest of the team members. For that behalf, a feature introduction meeting would be scheduled containing the development team leaders, architects and the Quality Assurance(QA) team members. Since the meeting is to make sure that the vision is clear, product management team would come up with real life examples to make their argument clear. Making it clear would take an effort in both sides, members who are invited to the meeting would be responsible for reading the documentation, understanding the feature as much as possible and taking notes if they have a problem. And the product team would make their best to answer those questions aiming to make sure everything is well understood. Then, when the feature itself is clear for team leads, architects and the QA team, invitees would start working on shaping their side of the sprint. For instance, development team leads would make preparation to transfer the knowledge they have on the feature by scheduling a second meeting, which is called as grooming, containing their team members to make the diffraction of the feature into stories and tasks. On the other hand, QA team would complete their own study to come up with fucntional and edge cases to run their tests. After those are completed, second meeting would be held and the assignment process would be completed. Assignment process contains assigning a specific story or task to some individual team member on a board, in which the board would be used to track status of the sprint. Parallel to that process, QA tem members would create their own tasks, relate it to the stories with their manual test case links. For manual test cases to be written, a platform such as "TestRail" could be used. A critical update would be necessary before starting the issues, due dates on the development tasks. Due Dates are important on when to complete the development and to deliver it to the test team for tests to be started. When due dates are entered on the development side, a schedule can be made on the test team on when to start&complete the tests. When every precondition is satisfied, sprint initiation document would be created by Program Manager and sign-offs would be asked by team members. When sign-offs are completed, sprint would be started by the Program Manager. During the sprint cycle, having the status updated on the board would have a critical priority. When the development is ready to be delivered onto the test side, status would be updated (ex. "To Verify") and the tests start. When the tests are completed, if there is any bug found, documentation(Bug initiation) should be well designed. It should be confirmed that anyone who does not know the flow to follow can easily understand the problem and how to reproduce it. Another critical issue related to this process would be making sure the failure is reflected via TestRail status and also Bug should be linked to the story and story status should be updated by the test team. When the problem is solved status should once again be updated and retest should be made. If there is no problem left, story should be closed by test team via changing the status(ex: "Done")
  
 ### On which stages a test should be scheduled?
 ### What is the type of the test that needs to be considered?
 ### What are the periodical tests that needs to be completed during the sprint cycle?
  
    Test should be made in two branches, Front End and Back End.
For the back end side, a test can be run when there is no precondition expected and the deploys are completed. There can be various types of test but first two to consider as a priority should be happy and invalid paths.
For the Front End side, there should be a test environment, and when the environment is ready to test, there should be functionality testing for the new features.
When it is completed informally, process can be followed by formal, regression and post production tests.
During those tests, the idea would be to first test the new features. Then, second, make sure the system is working efficienty after the new features are added.
Meaning, new comers should not break the existing ones.
That is a common problem on the development. Therefore, it is appropriate to make formal, regression and post production tests afterwards.
    
 ### Scenarios on the frond end test automation
 #### 1. City Hotels Search
 1.1. Go to setur.com.tr
 1.2. Click on "Otel" tab.
 1.3. Click on a city name under "Şehir Otelleri"
 #### 2. Custom Location
 2.1. Go to setur.com.tr
 2.2. Go to the footbar and click on a specific location like "Çeşme Otelleri"
 #### 3. Main Page Bilkent Hotel Search
 3.1. Go to setur.com.tr
 3.2. Type "Bilkent" on "otel veya konum yazın".
 3.3. Click on "Giriş Tarihi" and select an entrance day.
 3.4. Select the "Çıkış Tarihi" by selecting an exit day.
 3.5. Select the room count.
 3.6. Click on "2 yetişkin" if you have more or less number of people or if you have a children. 
 3.6.1. If you have more or less than 2 adults click on "2 Yetişkin" then make a selection over pop up by updating the count.
 3.6.2. If you have more or less than 2 adults and have 1 or more children click on "2 Yetişkin" then make a selection over pop up by updating the count on adults and then click on "Çocuk" and update the count over there as well. 
 3.6.3. Click "Uygula"
 3.7. Click "Ara".
 4. Safe Hotel List
 
    
    
