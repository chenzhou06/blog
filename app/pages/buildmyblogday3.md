title: Build My Blog - Day 3
published: 2015-3-13
tags: [programming]

I have been busy building my personal web blog for several days, but I can not 
feel satisfied with the look of my site till now.

I have wasted many hours searching online to solve trivial problems, such as
indenting `<ul>` elements, because the CSS package I used in my site, Materialize CSS，has forced any `<ul>` elements unindented and `<li>` elements prefixed with nothing.


	.article-content ul {
		margin-left: 2em;
	}
	.article-content ul li {
		list-style: disc inside;
	}


To cover the Materialize CSS' setting, I labelled the `div` where the markdown
files would be rendered with `article-content`. In this `div`, I set the margin at
the left side of `<li>` and resumed the bullets of list item style.

There are more things waited for me, the building of this site must be prolonged and improved little by little. Roma was not built in a day. During the process, 
I can sharp my programming skill enormously, I hope.

