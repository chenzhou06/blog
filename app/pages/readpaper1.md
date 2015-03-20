title: Reading Paper - Family Income
published: 2015-3-20
tags: [Economics, Learning]

I read a [paper](http://www.nber.org/papers/w11836) this week for the workshop in the weekend. Its author is a Korean
professor who worked at Seoul National University.

This paper discussed the inequality of the family income in the United States. The
author based his research on the data of *Annual Demographic Files on the March Current Population
Surveys (CPS)*.

# Analytical Framework

The author decomposed the family income into several sources.

First, he calculated the average annual income of households in a given income
decile by the formula below:
$$N = H_h W_h P_h + H_s W_s P_s \delta + Q$$
where \\(H_h , H_s , W_h~and~W_s\\) stand for the mean annual hours worked and
the mean hourly wage rate for employed heads and spouses, respectively. 
\\(P_h~and~P_s\\) stand for the employment rates for heads and spouse. \\(\delta\\)
is the fraction of households in which both husband and wife are present. \\(Q\\)
stands for the mean incomes from other sources.

Then he used the difference in the log of average family income between to income
deciles to measure the income inequality.
$$ N^*=ln[N^{TOP} ] - ln[N^{BOTTOM} ] $$

Combining the two equations above, we can get an equation:
$$ N^\* \approx \Phi_h \(H_h^\*+W_h^\*+P_h^\*\) + \Phi_s\(H_s^\*+W_s^\*+P_s^\*+\delta\)+\Phi_Q \(Q^\*\) $$
where \\( \Phi \\) stands for the weight of each of the three income sources.

By differentiating the equation above, we can obtain
$$ \Delta N^\* \approx \Phi_h\Delta H_h^\* + \Phi_h \Delta W_h^\* + \Phi_h \Delta P_h^\* $$
$$+ \Delta \Phi_h (H_h^\*+W_h^\*+P_h^\*) + \Phi_s \Delta H_s^\*$$
$$+\Phi_s \Delta +W_s^\*+ \Phi_s \Delta P_s^\* + \Phi_s \Delta \delta^\*$$
$$+ \Delta \Phi_s (H_s^\* + W_s^\* + P_s^\* + \delta^\*)$$
$$+ \Phi_Q \Delta Q^\* + \Delta \Phi_Q Q^\* $$

In this equation, the items at the right side stand for relative contribution of
the different components in family income to the rise of the inequality of family
income.

# Main Results

The main discovery is that the disparity in **other incomes (Q)** accounts for 29%
of the rise in the difference in income between the top 10th and bottom 10th families.

The second cause to the rise of inequality is employment and hours worked, which
explained 28% of the rise in the family income inequality.

Structural changes in wages, which has been regarded as the culprit of the rise of 
the inequality, accounted for less than a quarter of the rise in the measure of 
family income inequality.

For the upper half of the income distribution, wage changes were the dominant cause.
Changing head's wages explained more than half of the rise in the difference between
in incomes of the top 10 percent families and the average income.

However, for the lower half of the income distribution, changes in labor supply
and other incomes were the principal causes of the growing inequality in family
income.

# Head v.s. Householder

In this paper, 'Head' was used without any explanation. I couldn't know the author's
meaning by the word 'head'. In the CPS' meta-data documents I found some hints
which said 'head' has not been used from 1980s, they used 'householder' instead.
The 'householder' was the person in whose name the house the family was owned or
rented.
> The householder refers to the person
(or one of the persons) in whose name the housing
unit is owned or rented (maintained) or, if there is no
such person, any adult member, excluding roomers,
boarders, or paid employees. If the house is owned or
rented jointly by a married couple, the householder
may be either the husband or the wife. The person
designated as the householder on the file is the
"reference person" on the CPS-260 control card to
whom the relationship of all other household members,
if any, is recorded.

A householder could be either man or woman. But the author of this paper referred
'head' as man implicitly. He called the spouse wife several times in the context
of talking spouse's wage. I thought we should pay attention to this.

