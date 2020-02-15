import React from 'react';
import Gallery from 'react-photo-gallery';
import pic1 from '../Image/pic2.jpg';
import pic2 from '../Image/predictions_team.jpg';
import pic3 from '../Image/pic3.jpg';
import pic4 from '../Image/pic4.jpg';
import pic5 from '../Image/pic5.jpg';
import pic6 from '../Image/pic6.jpg';




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
    width: 20,
    height: 15
  },
  {
    src: pic2,
    width: 40,
    height: 30
  },
  {
    src: pic3,
    width: 4,
    height: 3
  },
  {
    src: pic5,
    width: 4,
    height: 3
  },
  {
    src: pic4,
    width: 4,
    height: 3
  },
  {
    src: pic6,
    width: 4,
    height: 3
  },
];