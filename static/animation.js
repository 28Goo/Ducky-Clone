//Preload
const tl = gsap.timeline({defaults: {ease: 'power1.out'}});

tl.to('.hideText', {y: '0%', duration: 1, stagger: 0.25});
tl.to('.slider', {y: '-100%', duration: 1, delay: 0.5});
tl.to('.intro', {y: '-100%', duration: 1}, '-=1');
tl.fromTo('header', {opacity: 0}, {opacity: 1, duration: 1});
tl.fromTo('.ducky', {x: '-300%'}, {x: '0%', duration: 1}, '-=1');
tl.fromTo('.mech', {x: '100%'}, {x: '0%', duration: 1}, '-=1');

//Animate scrolling effect of title
window.addEventListener('scroll', () => {
    document.body.style.setProperty('--scroll', window.pageYOffset / (document.body.offsetHeight - window.innerHeight));
}, false);
