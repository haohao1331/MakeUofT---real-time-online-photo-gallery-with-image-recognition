export interface Post {
	userName: string
	pic: string
	date: Date
	caption?: string
}

export type Feed = string[]

export interface InstaDataFormat {
	posts: Record<string, Post>
}

const result: InstaDataFormat = {
	posts: {
		post0: {
			userName: 'alan',
			pic: '/assets/post/1.1.png',
			date: new Date('2030-04-01T22:39:11.983'),
			caption: 'Another Alan? Recently received this figurine from Orbiseed in our corporate event. 3D printing has sure taken a giant leap since the early 2010s! Not sure if I have a good place to display this guy anywhere in my house!',
		},
	}
}

export default result
