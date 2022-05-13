<template>

	<div class="max-w-sm rounded overflow-hidden shadow-lg">
		<div class='poster-wrapper'>
			<img class="poster" :src='`${URL}${movie.poster_path}`' alt="Poster Image">
		</div>
		<div class="px-6 py-4">
			<div class="font-bold text-xl mb-2">{{ movie.title }}</div>
			<p class="text-gray-700 text-base word">
				{{ movie.overview }}
			</p>
		</div>
	</div>

</template>

<script>

export default {
	name: 'MovieCard',
	props: {
		movie: Object,
	},
	data: function() {
		return {
			URL: 'https://www.themoviedb.org/t/p/w1280'
		}
	}
}
</script>

<style>
	.poster-wrapper {
		position: relative;
		width: 100%;
		height: 0;
		padding-bottom: 150%;
		overflow: hidden;
	}
	.poster {
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
	}

	.word {
		font-weight: bolder;
		overflow: hidden;
		text-overflow: ellipsis;
		white-space: normal;
		word-wrap: break-word;
		display: -webkit-box;
		-webkit-line-clamp: 4 ;
		-webkit-box-orient: vertical;
	}
</style>