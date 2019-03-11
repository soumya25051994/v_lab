# v_lab
Value Lab codding challange

1. Create a model Track.

Created model with name "Track" with a field "track_name".

2. Each question belongs to a particular track. Update Question model to reflect this relationship.

Added and new ForeignKey field "tracker" in question model 

3. Create endpoint to perform CRUD operations for track.

http://localhost:8000/api/tracks/ - For GET and POST
http://localhost:8000/api/tracks/1/ - For UPDATE and DELETE
View Name : TrackViewSet

4. Create an API endpoint to fetch a list of all questions belonging to a particular track.

http://localhost:8000/api/questions/track/2/date_list/
(Here 2 is the tracker id)
View Name: getQuestionsByTrack

5. Create a model to map a question with choice which will considered as correct answer for the question.

Created a model "AnswerValidator" with two ForeignKey fields "question" and "answer". This model will save the question id with its respective correct answer from choices.

By using the below enpoints we can perform CURD operations for the model
http://localhost:8000/api/getAnswers/
http://localhost:8000/api/getAnswers/1/
View Name : AnswerValidatorViewSet


6. Create an API endpoint to fetch count of total correct answers and count of total wrong answers for a question.

http://localhost:8000/api/getAnswerStat/5/date_list/
(Here 5 is the question id)
View Name: getAnswerStat

No extra module required.



