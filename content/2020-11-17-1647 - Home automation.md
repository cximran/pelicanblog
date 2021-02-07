---
title: My foray into home automation with home assistant 
date:  2021-02-06 15:35:53
category: home automation
tags: home automation, home assistant, docker 
description: Articulating my first few steps into home automation.
status: published 
---
This post talks about my first foray into home automation. 
## Motivation 

Strangely enough, there was one thing that motivated this entire adventure. Our home has a set of lights on the porch that need to get turned on every night. After a few weeks of manually turning them on (or forgetting to turn them off once day breaks), I broke down and decided that I would find a solution. Not content with a simple programmable timer, I wanted something that would turn the lights on at sunset and off at sunrise - without having to reprogram it every few months to account for seasonal changes. This was all the justification I needed to dig into home automation. 

## Fundamentals  

The first thing that I did before even starting along this journey was understand the *basics* of how the various pieces of equipment work inside my home. For this, I leaned heavily on Charlie Wing's book, [How Your House Works - A Visual Guide](https://amzn.to/2XSvrRq). The book provides a bunch of easy to interpret diagrams that clearly lay out how different components work - such as plumbing systems, light switches, HVAC, and even individual appliances like dishwashers, garbage disposals, and vacuum cleaners. While most people probably don't need such a rudimentary overview of all these things, I find it essential as a first-time home owner with very few "handy" skills. Most importantly, Wing lays out everything and makes no assumptions about existing knowledge - something that I found **essential**. 

  <img src="{static}/images/wing-book-sample.png" class="img-responsive" alt="A Sample image from Charlie Wing's book depicting a diagram of a circuit breaker box">

Using the diagrams from Wing's book (plus a few other youtube tutorials on the topic) I quickly got up to speed on the basic electrical system in our house - including spending **way** too much time trying to demystify [3 and 4 way switch](https://en.wikipedia.org/wiki/Multiway_switching) combinations. 


## Hardware 

Of course, when working with *anything* related to electrical systems, if you're at all uncomfortable with it - call your local electrician.

In terms of hardware for the installation, here's what I used: 

### Tools 

- [Battery powered screwdriver](https://amzn.to/3oTv3Nn), to deal with electrical boxes 
- [Non-contact voltage tester](https://amzn.to/3cMhE7x), to make sure that there was to current running through anything I was working on 
- [Wire stripper](https://amzn.to/2YUa6qY), to strip, cut, and bend wires when needed 
- [Wire nuts](https://amzn.to/2N36L6w), to connect wires together 
- [Romex indoor electrical wire](https://amzn.to/2YP7xGM). I purchased a roll of the wire so that I could have a lot of extra wire available to me in the event that I needed to run an extra neutral wire or something like that. 
- [Head lamp](https://amzn.to/3aKhTx4). When you turn power off at the breaker, you're also likely to lose any of the light in the room so a head lamp is a necessity. 

### Smart Components 

Of course, a smart home doesn't work without smart components, and I decided to have the majority of the components on a local Z-wave based network. I picked Z-wave for a few reasons, but the biggest one was that I didn't want to have my smart home peripherals reliant on a potentially spotty wifi network. Additionally, one of the big advantages I saw with Z-wave was that each Z-wave device functions as a repeater within the overall network, so a flipped switch on the top floor has an easy path to the home server in the basement. I *did*, however, have to resort to wifi when looking for smart light bulbs. I ultimately resorted to buying 6 [TP-Link KL130 RGB Bulbs](https://amzn.to/3tAxgRy) when they were on sale. The bulbs actually work really well and adding colored lighting to a space really does wonders for atmosphere. 

- [Inovelli 3-way Z-wave rocker switch](https://amzn.to/3tsvUYS)
- [Zooz 3-way Z-wave toggle switch](https://amzn.to/3tyeWbv)
- [Zooz Z-wave smart plug](https://amzn.to/3aDwAlL), which is connected to a bedroom fan

Between Inovelli and Zooz, I would personally pick Zooz as a smart switch brand to beat. While both the Inovelli and Zooz switches were easy to configure, the Inovelli switch appeared to have way more configuration options (e.g. customizing the LED color on the switch) that in my opinion didn't justify the price delta. 

I'm not going to elaborate too much on installing the switches since there are way better tutorials out there, particularly on [Youtube](https://www.youtube.com/watch?v=PXRqaDX7A3A). 

### Home Server Hardware 

The "brains" behind the smart home operation is our humble home server, a 2019 Macbook Pro running Ubuntu in place of the original MacOS. Honestly, the big reason I went for Ubuntu was the fact that it I wanted to learn more about running a computer entirely through the command line. The server is connected to our home network using a USB-C to ethernet adapter, and it is also connected to a [Zooz USB Z-wave stick](https://amzn.to/2YURyXE) that communicates with the local Z-wave network. 

## Software 

The heart of the home automation setup we have at home is [Home Assistant](https://www.home-assistant.io/). I went with Home Assistant for the same reason I installed Ubuntu on the Macbook for the home server - I wanted to tinker! At the same time, I also wanted to learn a bit more about [Docker](docker.com), so I decided to run Home Assistant within a Docker container alongside a few other home server applications. Here is a crudely drawn sketch of the overall setup: 

  <img src="{static}/images/homeassistant-docker-layout.png" class="img-responsive" alt="A crudely drawn image of my software setup">

For most of the software set up, I followed the [official documentation](https://www.home-assistant.io/docs/installation/docker/). Surprisingly, it was mostly plug and play. The big issues I had were making sure that the external devices going into the server were passed through to the Home Assistant container. I found [Jack Stromberg's tutorial](https://jackstromberg.com/2020/02/home-assistant-z-wave-docker-raspberrypi/) on the subject to be very helpful. 

After the initial set up, I had to individually link each of the Z-wave switches to the system. This actually was extremely easy thanks to the Home Assistant mobile app, which allowed me to effortlessly add Z-wave nodes incrementally as I moved my way up from the switches closest to the server to the switches on the third floor of the house. 

In addition to running Home Asssitant, I also added a container for [Jellyfin](https://jellyfin.org/), our media server, and [Duplicati](https://www.duplicati.com/), which regularly backs up all of the Home Assistant configuration files/keys, encrypts them, and backs them up to a cloud drive. 

## What's next? 

So, right now I have Home Assistant controlling a few light switches and colored bulbs, but I have some ideas for what I want to do with the system in the coming months: 

- Flashing bulbs/lights when someone approaches the front door 
- Humidity/temperature sensors that alert us when there's a potential leak or heater being left on 
- Motion activated lights that slowly dim on and off when people walk within certain rooms. 

I'm really excited to keep mucking around with this - it's been quite the education! 