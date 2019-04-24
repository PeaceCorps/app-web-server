from django.db import models

class FirstAideAPI(models.Model):
	
	# Defining variables for creating choices for post_id field
	ADDED_SOON='added-soon'
	SEEKING_STAFF_SUPPORT='seeking-staff-support'
	SERVICES_AFTER_ASSAULT='services-after-assault'
	PEACE_CORPS_COMMITMENT='peace-corps-commitment'
	CONFIDENTIALITY='confidentiality'
	RADAR='radar'
	SEXUAL_PREDATORS='sexual-predators'
	SAFETY_PLAN_BASICS='safety-plan-basics'
	UNWANTED_ATTENTION='unwanted-attention'
	BYSTANDER_INTERVENTION='bystander-intervention'
	COMMON_QUESTIONS='common-questions'
	SAFETY_PLAN_WORKSHEET='safety-plan-worksheet'
	SEXUAL_ASSAULT='sexual-assault'
	SEXUAL_ASSAULT_MORE='sexual-assault-more'
	GLOSSARY='glossary'
	POLICY_SUMMARY='policy-summary'
	FURTHER_RESOURCES='further-resources'
	IMPACT_OF_ASSAULT='impact-of-assault'
	HELP_A_FRIEND='help-a-friend'
	MYTHBUSTERS='mythbusters'
	SEXUAL_HARRASMENT='sexual-harassment'

	# Choices attribute requires a tuple
	POST_ID_CHOICES=((ADDED_SOON, 'added-soon'),(SEEKING_STAFF_SUPPORT, 'seeking-staff-support'),(SERVICES_AFTER_ASSAULT,'services-after-assault'),
		(PEACE_CORPS_COMMITMENT,'peace-corps-commitment'),(CONFIDENTIALITY,'confidentiality'),(RADAR,'radar'),(SEXUAL_PREDATORS, 'sexual-predators'),
		(SAFETY_PLAN_BASICS, 'safety-plan-basics' ),(UNWANTED_ATTENTION,'unwanted-attention'),(BYSTANDER_INTERVENTION, 'bystander-intervention'),(COMMON_QUESTIONS,'common-questions'),
		(SAFETY_PLAN_WORKSHEET,'safety-plan-worksheet'),(SEXUAL_ASSAULT,'sexual-assault'),(SEXUAL_ASSAULT_MORE,'sexual-assault-more'),(GLOSSARY,'glossary'),
		(POLICY_SUMMARY,'policy-summary'),(FURTHER_RESOURCES,'further-resources'),(IMPACT_OF_ASSAULT,'impact-of-assault'),(HELP_A_FRIEND,'help-a-friend'),(MYTHBUSTERS,'mythbusters'),
		(SEXUAL_HARRASMENT,'sexual-harassment'))
	
	post_id = models.CharField(max_length=30, choices= POST_ID_CHOICES)

	# Defining variables for creating choices for page_type field
	FULL_PAGE_CARD='full_page_card'
	MULTI_CARDS_PAGE='multi_cards_page'
	MULTI_SEGMENT_PAGE='multi_segment_page'
	MULTI_SEGMENT_VERTICAL_PAGE='multi_segment_vertical_page'

	TYPE_OF_PAGE_CATEGORY=((FULL_PAGE_CARD,'full_page_card'),(MULTI_CARDS_PAGE,'multi_cards_page'),( MULTI_SEGMENT_PAGE,'multi_segment_page'),(MULTI_SEGMENT_VERTICAL_PAGE, 'multi_segment_vertical_page'))

	page_type = models.CharField(max_length= 30, choices=TYPE_OF_PAGE_CATEGORY)
	title = models.CharField(max_length=200, null = False)
	card_content = models.CharField(max_length= 5000, null= False)

	# Name to be shown for a particular instance of this type of model
	def __str__(self):
		return self.title

	# Name to be shown on the home page of the admin view for the collective set of model instances
	class Meta:
		verbose_name = 'First Aide API'

