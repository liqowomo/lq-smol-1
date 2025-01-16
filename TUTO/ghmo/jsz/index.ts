/*
Run this model in Javascript

> npm install openai
*/
import OpenAI from 'openai'
import fs from 'fs'

// To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings.
// Create your PAT token by following instructions here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
const token = process.env['GITHUB_TOKEN']

export async function main() {
	const client = new OpenAI({
		baseURL: 'https://models.inference.ai.azure.com',
		apiKey: token,
	})

	// This is the long ass question
	let question =
		'Describe the highest most valuable bugs in bug bounty hunting for webapps'

	const response = await client.chat.completions.create({
		messages: [
			{role: 'system', content: ''},
			{role: 'user', content: question},
		],
		model: 'gpt-4o',
		temperature: 1,
		max_tokens: 4096,
		top_p: 1,
	})

	const myrez = response.choices[0].message.content

	fs.writeFile('output.txt', myrez ??, (err) => {
		if (err) {
			console.error(err)
		} else {
			console.log('Content written to output.txt')
		}
	})
}

main().catch((err) => {
	console.error('The sample encountered an error:', err)
})
