#!/usr/bin/node
const STARTING_POKER_CHIPS = 100; // points
const PLAYERS = 3;
const NO_OF_STARTER_CARDS = 2;

const playerOneName = 'Chloe';
const playerTwoName = 'Jasmine';
const playerThreeName = 'Jen';

let playerOnePoints = STARTING_POKER_CHIPS;
let playerTwoPoints = STARTING_POKER_CHIPS;
let playerThreePoints = STARTING_POKER_CHIPS;

playerOnePoints -= 50;
playerTwoPoints -= 25;
playerThreePoints += 75;

console.log(`Welcome to Texas Hold'em. The championship title will be awarded to one of these three players: ${playerOneName}, ${playerTwoName} and ${playerThreeName}. Each player has ${STARTING_POKER_CHIPS} in their pot. We have an exciting game ahead of us. May the best player win!`);

let gameHasEnded = false;

gameHasEnded = ((playerOnePoints + playerTwoPoints) === 0) || // three has won
               ((playerTwoPoints + playerThreePoints) === 0) || // one has won
               ((playerOnePoints + playerThreePoints) === 0); // two has won
console.log('Game has ended: ', gameHasEnded);