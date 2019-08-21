import os
#import secrets
#from PIL import Image
from collections import OrderedDict 
from flask import render_template, url_for, flash, redirect, request, abort
from coded import app

courses = {
	'iOS-Dev': {
		'title': 'iOS-Dev',
		'desc': 'In the iOS course, instructor Sanaan Akhter will be \
				 introducing you to the development of iOS applications \
				 through the creation of an application of your own!',
		'author': 'Sanaan Akhter',
		'playlists': {
			'Your First App': {
				'This Is Michigan': 'UqoJmSF235E',
				'THON 2016 Promo': 'z-Bk09yXVBo',
				'THON 2016 Weekend Recap': 'oh3vsFDIa7U',
				'THON 2017 Promo': '14-j4CvRGIg',
				'THON 2017 Weekend Recap': 'oh3vsFDIa7U',
				'THON 2018 Promo': '14-j4CvRGIg'
			},
			'Swift Basics': {
				'This Is Michigan': 'UqoJmSF235E',
				'THON 2016 Promo': 'z-Bk09yXVBo',
				'THON 2016 Weekend Recap': 'oh3vsFDIa7U'
			},
			'iOS Game App': {
				'This Is Michigan': 'UqoJmSF235E',
				'THON 2016 Promo': 'z-Bk09yXVBo',
				'THON 2016 Weekend Recap': 'oh3vsFDIa7U',
				'THON 2017 Promo': '14-j4CvRGIg',
				'This Is ichigan': 'UqoJmSF235E',
				'THON 2018 Promo': 'z-Bk09yXVBo',
				'THON 2017 Weekend Recap': 'oh3vsFDIa7U'
			}
		},
		'sizes': {
			'Your First App': '6',
			'Swift Basics': '3',
			'iOS Game App': '7'
		}
	},
	'Web-Dev': {
		'title': 'Web-Dev',
		'desc': 'HTML & CSS are at the core of every website \
				 on the internet today.\n\
				 With this CodEd course, you will create your \
				 first website, learn the basics of HTML & CSS, \
				 and create a more complex blog website.\n\
				 Before starting this course, be sure to download \
				 Atom, Sublime Text or any other free text editor \
				 of your choice.',
		'author': 'Chinmay Savanur',
		'playlists': {
			'Your First Website':  {
				'Part 1: Getting Started': 'JIe7RGdv2js',
				'Part 2: Headers & Links': '4iSQF5gpNTo',
				'Part 3: Changing Color': '6WHR33fx02Q'
			},
			'HTML Basics': {
				'Part 1: Elements & Attributes': 'voRgQ2e9SBo',
				'Part 2: Paragraphs & Links': 'W1dHTSTtCrQ',
				'Part 3: Images, iFrames & IDs': 'jQ_SYDm5UPc',
				'Part 4: Styles & Text Formatting': 'KZP7h3SUG6I',
				'Part 5: Tables, Lists & Blocks': 'ixE2Q6Yv8ig',
				'Part 6: Responsive Web': 'nT9lJAqsblk'
			},
			'CSS Basics': {
				'Part 1: Inline, Internal & External': 'odcDl7iboCQ',
				'Part 2: Text, Align & Background': '8H3mgfzx8EY',
				'Part 3: The Box Model': 'ARC1kZOrDmQ',
				'Part 4: Tables': 'ZrYWqT2KmjI',
				'Part 5: Navigation Bar': 'RkNowfRf-Yc'
			},
			'Blog Website': {
				'Part 1: Getting Started': 's2kAhEc5iYk',
				'Part 2: Adding Content': 'U5HmF41bcfg',
				'Part 3: Navigation Bar': 'CaPu8_589gM',
				'Part 4: Blog Entries': '97VrISVq02Y',
				'Part 5: Gallery': '7b_H_33HZik'
			}
		},
		'sizes': {
			'Your First Website': '3',
			'HTML Basics': '6',
			'CSS Basics': '5',
			'Blog Website': '5'
		}
	},
	'Java': {
		'title': 'Java',
		'desc': 'In this introduction to programming in java course, \
				 Sara WHitlock will cover the same topics as the \
				 AP Computer Science.',
		'author': 'Sara Whitlock',
		'playlists': {
			'Your First Program': {
				'This Is Michigan': 'UqoJmSF235E',
				'THON 2016 Promo': 'z-Bk09yXVBo',
				'THON 2016 Weekend Recap': 'oh3vsFDIa7U'
			},
			'Java Basics': {
				'This Is Michigan': 'UqoJmSF235E',
				'THON 2016 Promo': 'z-Bk09yXVBo',
				'THON 2016 Weekend Recap': 'oh3vsFDIa7U',
				'THON 2019 Promo': 'z-Bk09yXVBo',
				'THON 2019 Weekend Recap': 'oh3vsFDIa7U',
				'THON 2020 Weekend Recap': 'oh3vsFDIa7U'
			},
			'Java Applications': {
				'This Is Michigan': 'UqoJmSF235E',
				'THON 2016 Promo': 'z-Bk09yXVBo',
				'THON 2016 Weekend Recap': 'oh3vsFDIa7U'
			}
		},
		'sizes': {
			'Your First Program': '3',
			'Java Basics': '6',
			'Java Applications': '3'
		}
	},
	'C++': {
		'title': 'C++',
		'desc': 'C++ is a high-level object-oriented coding language \
				 taught at many top-ranked Universities around the \
				 world and a key skill to be included on a resume.\n\
				 With this CodEd course, you will first learn the \
				 syntax of the language followed by an short series \
				 exploring classes as data structures and their \
				 importance in C++.\n\
				 Before starting this course, be sure to download \
				 XCode if you are on an Apple OS or Visual Studio Code \
				 on a Microsoft or Linux OS.',
		'author': 'Jared Miller',
		'playlists': {
			'Basics':  {
				'Part 1: Creating "Hello World!"': 'ikYXSabw9V0',
				'Part 2: Output & Comments': 'p-vsNAp6M6w',
				'Part 3: Variables & Input': 'Oze4Rja9gVw',
				'Part 4: Functions': 'fliui3TTFCc',
				'Part 5: Scope': 'yYQmJUEy91U',
				'Part 6: Math Operators': 'habMcH1SaQc',
				'Part 7: String Functions': 'OD3-5j7MMkI',
				'Part 8: Booleans & Conditionals': 'ys5mCH8LCMU',
				'Part 9: If Statements': 'N4HRY-QUifU',
				'Part 10: While Loops': 'O3udG8-e4tE',
				'Part 11: For Loops': 'RHh2bQS3DtU',
				'Part 12: Arrays': 'Nn9nqV1H3Jg',
				'Part 13: Vectors': '3joCytKMix0'
			},
			'Classes':  {
				'Part 1: Intro & Writing a Class': 'SZZtGB0f4Rg',
				'Part 2: Header & Class File Syntax': 'xLtXhQAbuJ0',
				'Part 3: Initializer Lists & RME': 'IlTuQiaHPRs',
			}
		},
		'sizes': {
			'Basics': '13',
			'Data Structures': '3'
		}
	}
}

teammembers = {
	'Jared Miller': {
		'Here @ CodEd': 'Founder, Webmaster, C++ Instructor',
		'Education': 'University of Michigan \'22',
		'Major': 'Computer Science (Honors)',
		'Outside of Class': 'Jared is on the planning team for\
							 Dance Marathon at the University of Michigan, \
							 enjoys reading and has a passion for \
							 impacting the world through technology.'
	}, 
	'Chinmay Savanur': {
		'Here @ CodEd': 'Web-Dev Instructor',
		'Education': 'University of Michigan \'23',
		'Major': 'Computer Science (Honors)',
		'Outside of Class': 'Chinmay enjoys learning all about STEM \
							 and is an aspiring web-developer. He also \
							 loves playing frisbee and basketball \
							 with his friends.'
	}, 
	'Nick Anderson': {
		'Here @ CodEd': 'Marketing',
		'Education': 'Villanova University \'22',
		'Major': 'Computer Science',
		'Outside of Class': 'Nick is a Midshipman in Naval ROTC and enjoys \
							 practicing Judo, working out, debating \
							 politics and studying Mandarin Chinese.'
	}, 
	'Jared Glassband': {
		'Here @ CodEd': 'Marketing',
		'Education': 'Cornell University \'22',
		'Major': 'Mathematics & Physics',
		'Outside of Class': 'Jared enjoys reading a variety of fiction books—his \
							 favorite being "The Hitchhiker\'s Guide to \
							 the Galaxy" series—and loves spending time with \
							 his friends at Cornell sporting events.'
	}, 
	'Harsh Padhye': {
		'Here @ CodEd': 'Java Instructor',
		'Education': 'University of Virginia \'23',
		'Major': 'Computer Science & Mathematics (Honors)',
		'Outside of Class': 'Harsh is an aspiring musician who plays \
							 the guitar and enjoys rock, edm, hip-hop \
							 and jazz. He also plays soccer, ultimate \
							 frisbee and likes distance running.'
	}
}

@app.route("/")
@app.route("/home")
def home():
	browser = request.user_agent.browser
	if browser == 'msie':
		flash('Internet Explorer is not yet supported. Please use a different browesr.', 'danger')
		return redirect(url_for('unsupported'))
	return render_template('home.html', teammembers=teammembers)

@app.route("/unsupported")
def unsupported():
	browser = request.user_agent.browser
	if browser != 'msie':
		return redirect(url_for('home'))
	return render_template('unsupported.html')

@app.route("/course/<string:title>")
def course(title):
	browser = request.user_agent.browser
	if browser == 'msie':
		flash('Internet Explorer is not yet supported. Please use a different browesr.', 'danger')
		return redirect(url_for('unsupported'))
	desc = courses[ title ].get("desc")
	author = courses[ title ].get("author")
	auth_desc = teammembers[ author ]
	playlists = courses[ title ].get("playlists")
	sizes = courses[ title ].get("sizes")
	return render_template('course.html', title=title, desc=desc.split('\n'), 
						   author=author, auth_desc=auth_desc, 
						   playlists=playlists, sizes=sizes)

@app.route("/soon/<string:title>")
def soon(title):
	browser = request.user_agent.browser
	if browser == 'msie':
		flash('Internet Explorer is not yet supported. Please use a different browesr.', 'danger')
		return redirect(url_for('unsupported'))
	return render_template('soon.html', title=title)

@app.route("/lesson/<string:title>/<string:lesson>/<string:current_vid>")
def lesson(title, lesson, current_vid):
	browser = request.user_agent.browser
	if browser == 'msie':
		flash('Internet Explorer is not yet supported. Please use a different browesr.', 'danger')
		return redirect(url_for('unsupported'))
	desc = courses[ title ].get("desc")
	playlists = courses[ title ].get("playlists")
	sizes = courses[ title ].get("sizes")
	course_lesson = title + " " + lesson
	return render_template('lesson.html', title=title, lesson=lesson,
						   course_lesson=course_lesson, video = current_vid, 
						   playlists=playlists, sizes=sizes)










