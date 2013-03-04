$(document).ready(function(){

	resetViews();

	$('#btnAnalyze').click(function(){

		resetViews();
		$('#btnAnalyze').attr('disabled','disabled');
		$('#loadingDiv').html('<img src="assets/img/loading.gif">');

		var userName = $('#userNameInput').val();
		if(userName == ''){
			$('#loadingDiv').html('<div class="alert alert-error">The Twitter User Name you entered is not valid. Please try again.</div>');
			$('#btnAnalyze').removeAttr('disabled');
		}else{

			var ajaxData = {'userName': userName};
			var ajaxUrl = "cgi-bin/TwitterProfilerApp.cgi";

			$.ajaxSetup({
				cache: false,
			});

			$.ajax(ajaxUrl, {
				data: ajaxData,
				success: ajaxResponse,
				dataType: 'json'
			});

		}

	
	});

});

function resetViews(){
	$('#emotionalResultsDiv, #psychopathyResultsDiv, #spiritualResultsDiv, #consumerResultsDiv').html('');
	$('#emotionalResultsTitle').html('');
	$('#psychopathyresultsTitle').html('');
	$('#spiritualResultsTitle').html('');
	$('#consumerResultsTitle').html('');
	$('#emotionalResultsDiv, #psychopathyResultsDiv, #spiritualResultsDiv, #consumerResultsDiv').hide();
	$('.hideThis').show();
	$('.hiddenHr').html('');
	$('.footer').hide();
}

function ajaxResponse(data, textStatus, jqXHR){
	
	$('#btnAnalyze').removeAttr('disabled');

	if(data['error'] != null){		
		var error = data['error'];
		if(error == 'rateLimit'){
			error = '<div class="alert alert-error">Twitter rate limit exceeded. Unfortunately Twitter limits the amount of requests this App can make. Try again in an hour.</div>'
		}else{
			error = '<div class="alert alert-error">The Twitter User Name you entered is not valid. Please try again.</div>'
		}

		$('#loadingDiv').html(error);

	}else{

		console.log('Tweet Count: ' + data['tweetCount'] + ', Remaining Api Hits: ' + data['remainingApiHits'])

		$('#loadingDiv').html('');
		$('.hideThis').hide();
		$('.hiddenHr').html('<hr>');

		graphEmotionalResults(data['emotionResults']);
		graphPsychopathyResults(data['psychopathyResults']);
		graphSpiritualResults(data['spiritualResults']);
		graphConsumerResults(data['consumerResults']);

		$('.footer').show();
	}

	

}

function graphEmotionalResults(emotionResults){

	$('#emotionalResultsTitle').html('<h1>Emotional <small>Profile</small></h1>');
	$('#emotionalResultsDiv').show();

	var caringData = emotionResults['results']['Caring']['score'];
	var quietData = emotionResults['results']['Quiet positive']['score'];
	var negativeThoughtsData = emotionResults['results']['Negative thoughts']['score'];
	var agitationData = emotionResults['results']['Agitation']['score'];
	var reactiveData = emotionResults['results']['Reactive']['score'];
	var negativePassiveData = emotionResults['results']['Negative and passive']['score'];
	var positiveLivelyData = emotionResults['results']['Positive and lively']['score'];
	var positiveThoughtsData = emotionResults['results']['Positive thoughts']['score'];
	var negativeForcefulData = emotionResults['results']['Negative and forceful']['score'];
	var negativeControlData = emotionResults['results']['Negative and not in control']['score'];

	var graphData = [
		{ label: "Caring",  data: caringData, color: '#81DAF5'},
		{ label: "Positive Thoughts",  data: positiveThoughtsData, color: '#58ACFA'},
		{ label: "Positive and Lively",  data: positiveLivelyData, color: '#2E64FE'},
		{ label: "Quiet Positive",  data: quietData, color: '#0000FF'},
		{ label: "Agitation",  data: agitationData, color: '#F3F781'},
		{ label: "Reactive",  data: reactiveData, color: '#F7FE2E'},
		{ label: "Negative Thoughts",  data: negativeThoughtsData, color: '#F7D358'},
		{ label: "Negative and Passive",  data: negativePassiveData, color: '#FFBF00'},
		{ label: "Negative and Forceful",  data: negativeForcefulData, color: '#FF8000'},
		{ label: "Negative and not in Control",  data: negativeControlData, color: '#B40404'}
	];	

	$.plot($("#emotionalResultsDiv"), graphData, 
	{
		series: {
            pie: { 
                innerRadius: 0.5,
                show: true
            }
        },
		legend: {
			show: true
		}
	});

}

function graphPsychopathyResults(psychopathyResults){

	$('#psychopathyResultsDiv').show();

	var causeEffect = psychopathyResults['results']['Cause and effect']['score'];
	var disfluencies = psychopathyResults['results']['Material needs']['score'];
	var materialNeeds = psychopathyResults['results']['Disfluencies']['score'];
	var narcicism = psychopathyResults['results']['Narcisism']['score'];
	var totalScore = psychopathyResults['finalScore'];

	causeEffect = Math.round(causeEffect);
	causeEffect = causeEffect.toString() + '%';

	disfluencies = Math.round(disfluencies);
	disfluencies = disfluencies.toString() + '%';

	materialNeeds = Math.round(materialNeeds);
	materialNeeds = materialNeeds.toString() + '%';

	narcicism = Math.round(narcicism);
	narcicism = narcicism.toString() + '%';

	totalScore = Math.round(totalScore);
	totalScore = totalScore.toString() + '%';

	$('#psychopathyResultsDiv').load('psychopathyResults.html', function(){

		$('#causeEffectBar').css('width',causeEffect);
		$('#disfluenciesBar').css('width',disfluencies);
		$('#materialNeedsBar').css('width',materialNeeds);
		$('#narcicismBar').css('width',totalScore);
		$('#totalPsychBar').css('width',totalScore);

	});
	

}

function graphSpiritualResults(spiritualResults){

	$('#spiritualResultsTitle').html('<h1>Spiritual <small>Profile</small></h1><br><br>');
	$('#spiritualResultsDiv').show();

	var religionScore = spiritualResults['results']['Religion']['score']
	var christianityScore = spiritualResults['results']['Christianity']['score']
	var judaismScore = spiritualResults['results']['Judaism']['score']
	var buddhismScore = spiritualResults['results']['Buddhism']['score']
	var islamScore = spiritualResults['results']['Islam']['score']

	religionScore = religionScore * 5;
	christianityScore = christianityScore * 5;
	judaismScore = judaismScore * 5;
	buddhismScore = buddhismScore * 5;
	islamScore = islamScore * 5;

	arrayOfData = new Array(
		[religionScore,'Religion','#F7FE2E'],
		[christianityScore,'Christianity','#F7D358'],
		[judaismScore,'Judaism','#FFBF00'],
		[buddhismScore,'Buddhism','#FF8000'],
		[islamScore,'Islam','#B40404']
	); 	

	$('#spiritualResultsDiv').jqBarGraph({ data: arrayOfData, width: 800, height: 300, showValues: false});

}

function graphConsumerResults(consumerResults){
	
	$('#consumerResultsDiv').show();

	var words = consumerResults['results']['Brands']['keyWords'];
	var word_array = []

	for (var key in words){
		var temp = {text: key, weight: words[key]};
		word_array.push(temp)
	}

	$('#consumerResultsTitle').html('<h1>Consumer <small>Profile</small></h1><br><br>');	
    $("#consumerResultsDiv").jQCloud(word_array);

}