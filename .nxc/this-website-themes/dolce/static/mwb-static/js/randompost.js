const websiteroot = "{{websiteroot}}"
function randomPostLink() {
  return `${websiteroot}`lunr_posts[Math.floor(Math.random() * lunr_posts.length)].link;
}
