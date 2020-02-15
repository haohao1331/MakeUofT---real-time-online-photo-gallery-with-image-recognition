import React from 'react';
import Gallery from 'react-photo-gallery';
import pic1 from '../Image/predictions_team.jpg'

export default class Sample extends React.Component {
    render() {
	return (
	    <Gallery photos={PHOTO_SET} />
	);
    }
}
const PHOTO_SET = [
  {
    src: pic1,
    width: 4,
    height: 3
  },
  {
    src: '../Image/predictions_team.jpg',
    width: 1,
    height: 1
  }
];