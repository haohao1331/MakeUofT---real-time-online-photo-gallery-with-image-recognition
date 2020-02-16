import React from 'react';
import Gallery from 'react-photo-gallery';
import pic1 from '../Image/pic1.jpg';
import a4020308478561 from '../Image/a4020308478561.jpg';
import a7261881436758 from '../Image/a7261881436758.jpg';
import a3452634823694 from '../Image/a3452634823694.jpg';
import a1253913856332 from '../Image/a1253913856332.jpg';
import a386437340731 from '../Image/a386437340731.jpg';
import a2351156158585 from '../Image/a2351156158585.jpg';
import a936426174968 from '../Image/a936426174968.jpg';
import a955617133937 from '../Image/a955617133937.jpg';
import a7180543149469 from '../Image/a7180543149469.jpg';
import a713633332404 from '../Image/a713633332404.jpg';






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
    src: a4020308478561,
    width: 4,
    height: 3
  },
  {
    src: a7261881436758,
    width: 4,
    height: 3
  },
  {
    src: a3452634823694,
    width: 4,
    height: 3
  },
  {
    src: a1253913856332,
    width: 4,
    height: 3
  },
  {
    src: a386437340731,
    width: 4,
    height: 3
  },
  {
    src: a2351156158585,
    width: 4,
    height: 3
  },
  {
    src: a936426174968,
    width: 4,
    height: 3
  },
  {
    src: a955617133937,
    width: 4,
    height: 3
  },
  {
    src: a7180543149469,
    width: 4,
    height: 3
  },
  {
    src: a713633332404,
    width: 4,
    height: 3
  },
];