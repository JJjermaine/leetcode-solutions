<h1>2532 - Remove Letter To Equalize Frequency</h1><h2>Difficulty: Easy - <a href="https://leetcode.com/problems/remove-letter-to-equalize-frequency/">remove-letter-to-equalize-frequency</a></h2><p>You are given a <strong>0-indexed</strong> string <code>word</code>, consisting of lowercase English letters. You need to select <strong>one</strong> index and <strong>remove</strong> the letter at that index from <code>word</code> so that the <strong>frequency</strong> of every letter present in <code>word</code> is equal.</p>

<p>Return<em> </em><code>true</code><em> if it is possible to remove one letter so that the frequency of all letters in </em><code>word</code><em> are equal, and </em><code>false</code><em> otherwise</em>.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>The <b>frequency</b> of a letter <code>x</code> is the number of times it occurs in the string.</li>
	<li>You <strong>must</strong> remove exactly one letter and cannot choose to do nothing.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> word = &quot;abcc&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> Select index 3 and delete it: word becomes &quot;abc&quot; and each character has a frequency of 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> word = &quot;aazz&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> We must delete a character, so either the frequency of &quot;a&quot; is 1 and the frequency of &quot;z&quot; is 2, or vice versa. It is impossible to make all present letters have equal frequency.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= word.length &lt;= 100</code></li>
	<li><code>word</code> consists of lowercase English letters only.</li>
</ul>
