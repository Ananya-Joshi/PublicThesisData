import os
questions = ["Whether or not someone's action showed love for his or her country", 
"Whether or not someone showed a lack of respect for authority",
"Whether or not someone violated standards of purity and decency",
"Whether or not someone was good at math",
"Whether or not someone cared for someone weak or vulnerable",
"Whether or not someone acted unfairly",
"Whether or not someone did something to betray his or her group",
"Whether or not someone conformed to the traditions of society" ,
"Whether or not someone did something disgusting",
"Whether or not someone was cruel",
"Whether or not someone was denied his or her rights",
"Whether or not someone showed a lack of loyalty",
"Whether or not an action caused chaos or disorder",
"Whether or not someone acted in a way that God would approve of"]

questions2 = ["Compassion for those who are suffering is the most crucial virtue.",
"When the government makes laws, the number one principle should be ensuring that everyone is treated fairly.",
"I am proud of my country's history.",
"Respect for authority is something all children need to learn.",
"People should not do things that are disgusting, even if no one is harmed. ",
"It is better to do good than to do bad.",
"One of the worst things a person could do is hurt a defenseless animal.",
"Justice is the most important requirement for a society.",
"People should be loyal to their family members, even when they have done something wrong.  ",
"Men and women each have different roles to play in society.",
"I would call some acts wrong on the grounds that they are unnatural.",
"It can never be right to kill a human being.",
"I think it's morally wrong that rich children inherit a lot of money while poor children inherit nothing.",
"It is more important to be a team player than to express oneself.",
"If I were a soldier and disagreed with my commanding officer's orders, I would obey anyway because that is my duty.",
"Chastity is an important and valuable virtue."]


def part1():
	for i in range(3, 17):

		print("<div class = \"question\">\n\tQ" + str(i) +": " + questions[i-3] + ": <strong><span id=\"demo" +str(i) + "\" , class = \"demo\"></span> </strong>\
					\n\t\t<div class=\"slidecontainer\">\n\
					  <input type=\"range\" min=\"0\" max=\"5\" value=\"3\" class=\"slider\" id=\"myRange\" oninput=\"myFunction(this, \'demo" + str(i) + "\')\">\
					\n\t\t</div>\
				\n</div>")
		print("")
		print("")


def part2():
	for i in range(17, 33):

		print("</br></br></br><div class = \"question\">\n\tQ" + str(i) +": " + questions2[i-17] + ": <strong><span id=\"demo" +str(i) + "\" , class = \"demo\"></span> </strong>\
					\n\t\t<div class=\"slidecontainer\">\n\
					  <input type=\"range\" min=\"0\" max=\"5\" value=\"3\" class=\"slider\" id=\"myRange\" oninput=\"myFunction2(this, \'demo" + str(i) + "\')\">\
					\n\t\t</div>\
				\n</div>")
		print("")
		print("")


part2()